import csv
import statsmodels.stats.multitest
from Bio import SeqIO
import scipy.stats
import os,glob
import numpy as np
import scipy
import re
from EssentialFinder.extras.possion_binom import PoiBin
from scipy.stats import binom_test
import multiprocessing
import matplotlib.pyplot as plt
import sys
import datetime

#associates a Tn5 insertion position with a gene (unique insertions and upstream/down regions) usgin a gff file as the annotation file and the pangenome as the gene name file, 
#giving also genes without any insertion and returning essential genes for a given pvalue

def inputs(argv):
    
    global variables
    variables=Variables()
    variables.directory = argv[0] #folder with the unique insertions file
    variables.strain = argv[1] #strain name, and annotation file name
    variables.annotation_type = argv[2]
    variables.annotation_folder = argv[3]
    variables.pan_annotation=argv[4]

    variables.output_name = variables.strain + "_alldomains"
    variables.true_positives = variables.annotation_folder + "/Truepositivs.csv"
    variables.true_negatives = variables.annotation_folder + "/Truenegativs_compiled.csv"

def path_finder():
    
    def sub_path_finder(folder,extenction,search):
        for filename in glob.glob(os.path.join(folder, extenction)):
            test1 = filename.find(search) 
            if test1 != -1: 
                return filename
    
    variables.insertion_file_path=sub_path_finder(variables.directory,'*.csv',"all_insertions")

    if variables.annotation_type == "gb":
        variables.annotation_file_paths=[sub_path_finder(variables.annotation_folder,'*.gb',variables.strain)]

    elif variables.annotation_type == "gff":
        variables.annotation_file_paths=[sub_path_finder(variables.annotation_folder,'*.gff',variables.strain)]
        variables.annotation_file_paths.append(sub_path_finder(variables.annotation_folder,'*.fasta',variables.strain))

        if len(variables.annotation_file_paths) < 2:
            print("Wrong file paths. Check file names") 

def output_writer(output_folder, name_folder, output_file):
    output_file_path = os.path.join(output_folder, name_folder + ".csv")
    with open(output_file_path, "w", newline='') as output:
        writer = csv.writer(output)
        writer.writerows(output_file)

class Variables():
    
    def motif_compiler(self):
            dna = ["A","T","C","G"]
            prog,di_motivs = [],[]
            for letter1 in dna:
                for letter2 in dna:
                    di_motivs.append(f"{letter1}{letter2}")
                    motiv = f"(?=({letter1}{letter2}))"
                    prog.append(re.compile(motiv, re.IGNORECASE))
            return prog,di_motivs

    def __init__(self,directory=None,strain=None,annotation_type=None,annotation_folder=None,pan_annotation=None,\
                 output_name=None,true_positives=None,true_negatives=None,\
                 insertion_file_path=None,annotation_file_paths=None,borders_contig={},orientation_contig={},\
                insertions_contig={},genome_seq={},genome_length=0,annotation_contig=None,total_insertions=None,\
                positive_strand_tn_ratio=None,transposon_motiv_count=None,transposon_motiv_freq=None,\
                chance_motif_tn=None,orientation_contig_plus={},orientation_contig_neg={}):
        
        self.directory = directory
        self.strain = strain
        self.annotation_type = annotation_type
        self.annotation_folder = annotation_folder
        self.pan_annotation = pan_annotation
        self.output_name = output_name
        self.true_positives = true_positives
        self.true_negatives = true_negatives
        self.domain_iteration = [1.1,2,4]#[1.1,2,4,8,16,32,64,128,256,512,1024,2048,4096] #""" make user defined """
        self.pvalue = 0.05 #""" make user defined """
        self.insertion_file_path = insertion_file_path
        self.annotation_file_paths = annotation_file_paths
        self.borders_contig = borders_contig
        self.orientation_contig = orientation_contig
        self.insertions_contig = insertions_contig
        self.genome_seq = genome_seq
        self.genome_length = genome_length
        self.annotation_contig = annotation_contig
        self.total_insertions = total_insertions
        self.positive_strand_tn_ratio = positive_strand_tn_ratio
        self.transposon_motiv_count = transposon_motiv_count
        self.transposon_motiv_freq=transposon_motiv_freq
        self.chance_motif_tn = chance_motif_tn
        self.orientation_contig_plus =orientation_contig_plus
        self.orientation_contig_neg = orientation_contig_neg
        self.regex_compile,self.di_motivs = self.motif_compiler()
        
    def normalizer(self):
        motif_genome = np.zeros(16)
        ##### Counts the entire motifv content of the genome; determining the probability of having an insertion in each motif    
        for key in self.genome_seq:
            atcg = count_GC([self.genome_seq[key]],self.regex_compile)
            for i, element in enumerate(motif_genome):
                motif_genome[i] = element + atcg[i] 
    
        #probability oh having a motif with a transposon in it
        self.chance_motif_tn = np.divide(self.transposon_motiv_count,motif_genome)
        for i, entry in enumerate(self.chance_motif_tn):
            if entry >=1:
                self.chance_motif_tn[i] = 0.999999
        return np.array([[n] for n in self.chance_motif_tn])

########
### Creates a class with all the recurrent info needed for processing each gene/domain using genbank files
#####    
    
class Storage():
    
    def __init__(self, gene=None, start=None, end=None, orientation=None, domains=None, identity=None, \
                 product=None, contig=None,matrix=None,domain_insertions_total=None, GC_content=None, \
                   domain_notes=None, motif_seq=None, subdomain_insert_orient_plus=None, \
                       subdomain_insert_orient_neg=None):
        
        self.gene = gene
        self.start = start
        self.end = end
        self.length = end - start
        self.orientation = orientation
        self.domains = domains
        self.identity = identity
        self.product = product
        self.contig = contig
        self.gene_insert_matrix = matrix
        self.domain_insertions_total = domain_insertions_total
        self.GC_content = GC_content
        self.domain_notes = domain_notes
        self.motif_seq = motif_seq
        self.subdomain_insert_orient_plus = subdomain_insert_orient_plus or dict()
        self.subdomain_insert_orient_neg = subdomain_insert_orient_neg or dict()

def gene_info_parser_genbank(file):
    basket = {}
    for rec in SeqIO.parse(file, "gb"):
        for feature in rec.features:
            if (feature.type == "CDS") or (feature.type == "RNA"):
                start = feature.location.start.position
                end = feature.location.end.position
                orientation = feature.location.strand
                identity = feature.qualifiers['locus_tag'][0]
                
                if 'product' in feature.qualifiers:
                    product = feature.qualifiers['product'][0]
                else:
                    product = feature.qualifiers['note'][0]
                    
                for key, val in feature.qualifiers.items():   
                    if "pseudogene" in key:
                        gene = identity
                        break #avoids continuing the iteration and passing to another key, which would make "gene" assume another value
                    elif "gene" in key:
                        gene = feature.qualifiers['gene'][0]
                        break #avoids continuing the iteration and passing to another key, which would make "gene" assume another value
                    else:
                        gene = identity
                        
                if orientation == 1:
                    orientation = "+"
                else:
                    orientation = "-"
                        
                basket[identity] = Storage(gene=gene,start=start,end=end,orientation=orientation,\
                                           identity=identity,product=product,contig=variables.annotation_contig)
                                   
    return basket
                     
def gene_info_parser_gff(file):
    basket = {}
    with open(file) as current:
        for line in current:
            GB = line.split('\t') #len(GB)
            if "#" not in GB[0][:3]: #ignores headers
                if GB[2] == "CDS": 
                    start = int(GB[3])
                    end = int(GB[4])
                    features = GB[8].split(";") #gene annotation file
                    feature = {}
                    for entry in features:
                        entry = entry.split("=")
                        feature[entry[0]] = entry[1].replace("\n","")
                    if "gene" in feature:
                        gene=feature["gene"]
                    else:
                        gene=feature["ID"]
                    
                    contig = GB[0]
                    orientation = GB[6] #orientation of the gene
                    basket[feature["ID"]] = Storage(gene=gene,start=start,end=end,orientation=orientation,\
                                                    identity=feature["ID"],product=feature["product"],contig=contig)

    ### associate a gene with a pan genome file
    if variables.pan_annotation != None:
        with open(variables.pan_annotation) as current:
            for line in current:
                line = line.split(',')
                gene = line[0]
                current_genes_set = set(line)
                for key in basket:
                    if basket[key].identity in current_genes_set:
                        basket[key].gene = gene
    return basket

def domain_resizer(domain_size_multiplier,basket):
    domain_size = int(variables.genome_length / variables.total_insertions * domain_size_multiplier)
    for key in basket:
        local_stop = [basket[key].start]
        start_iterator = basket[key].start
        end = basket[key].end
        
        divider = int((end - start_iterator) / domain_size)
        
        if divider >= 1:
            for i in range(divider):
                local_stop.append(start_iterator+domain_size) #creates all the subdomains
                start_iterator += domain_size
    
        if (end - (local_stop[-1] + domain_size)) > domain_size:
            del local_stop[-1]
        
        if local_stop[-1] != end:
            local_stop.append(end)
        local_stop.append(end) #the end of the gene is always required in duplicate
        basket[key].domains = local_stop
    return basket

def gene_insertion_matrix(basket):
    
    def contig_matrix_generator(orient,genome_orient_plus_matrix,genome_orient_neg_matrix,\
                                borders,genome_borders_matrix,inserts,genome_insert_matrix,contig):
    
        for j,local in enumerate(inserts):
            local = int(local-1)
            genome_insert_matrix[local]=1
            genome_borders_matrix[local]=borders[j]
            if orient[j] == "+":
                genome_orient_plus_matrix[local]=1
            else:
                genome_orient_neg_matrix[local]=1

        return genome_insert_matrix,genome_borders_matrix,genome_orient_plus_matrix,genome_orient_neg_matrix
    
    print("Compiling insertion matrix")

    for contig in variables.genome_seq:
        contig_size=len(variables.genome_seq[contig])
        genome_insert_matrix = np.zeros(contig_size,dtype=np.int8)
        genome_borders_matrix = np.zeros(contig_size,dtype='<U2')
        genome_orient_plus_matrix = np.zeros(contig_size,dtype=np.int8)
        genome_orient_neg_matrix = np.zeros(contig_size,dtype=np.int8)
        variables.orientation_contig_plus[contig] = {}
        variables.orientation_contig_neg[contig] = {}
        
        if len(variables.insertions_contig[contig]) != 0:
            inserts= np.array(variables.insertions_contig[contig])
            borders= np.array(variables.borders_contig[contig])
            orient = np.array(variables.orientation_contig[contig])
        else:
            inserts=np.zeros(contig_size,dtype=np.int8)
            borders=np.zeros(contig_size,dtype='<U2')
            orient=np.zeros(contig_size,dtype=np.int8)
            
        variables.insertions_contig[contig],\
        variables.borders_contig[contig],\
        variables.orientation_contig_plus[contig],\
        variables.orientation_contig_neg[contig]= \
        contig_matrix_generator(orient,genome_orient_plus_matrix,genome_orient_neg_matrix,\
                                borders,genome_borders_matrix,inserts,genome_insert_matrix,contig)

    for key in basket:
        start=basket[key].start-1
        end=basket[key].end-1
        for contig in variables.insertions_contig:#calculating local insertion transposon density in bp windows (size variable)
            if basket[key].contig == contig:
                basket[key].gene_insert_matrix = variables.insertions_contig[contig][start:end]

    return basket

def count_GC(seq, prog):
    result = []
    for motiv in prog:
        for insert in seq:
            result.append(len( [m.start() for m in re.finditer(motiv, insert)] ))  
    return result

def motiv_compiler(seq,prog):
    motiv_inbox = np.zeros(16)
    for s, insertion in enumerate(seq):
        if insertion != "":
            for i, motiv in enumerate(prog):
                if [m.start() for m in re.finditer(motiv, insertion)] != []:
                    motiv_inbox[i] =  motiv_inbox[i] + 1
                    break
    return motiv_inbox

def poisson_binomial(events,motiv_inbox,tn_chance):
    def chance_matrix(events,motiv_inbox,tn_chance):
        p_effective=np.array(())
        for i, (chance,number) in enumerate(zip(tn_chance,events)):
            for i in range(number):
                p_effective=np.append(p_effective,chance)
        sucess = np.sum(motiv_inbox)     
        if sucess > np.sum(events): #due to insertion redundancy (+ and - strand), sometimes there are more insertions than bp
            sucess = np.sum(events)
        return sucess, p_effective
    
    sucess,p_effective=chance_matrix(events,motiv_inbox,tn_chance)
    pb = PoiBin(p_effective) 
    
    return abs(pb.cdf(int(sucess))) #in some cases of highly biassed transposon, essential genes can be so significant that p < 0 (probably some bug on the poisson code)

def essentials(basket,variables):

    significant = []
    pvalues_list = []
    pvalue_orient_list = []

    #annexes all the genes which fit the criteria of essentiality
    for key in basket:
        insertions = basket[key].domain_insertions_total #total number of insertions in gene
        domain_motivs = basket[key].GC_content #number of each motif in the gene (sum is gene lenght)
        name = basket[key].gene
        domains = basket[key].domains[:-1]
        motiv_insertions = basket[key].motif_seq #number of each insertion per motif in the gene (sum is total insertions)
        orientation = basket[key].orientation
        start = basket[key].start
        
        total_insertions = sum(insertions)
        
        if total_insertions == 0: #gene has no insertions

            domain_part = "whole gene"
            ratio_orientation, orient_pvalue = "N/A", "N/A"
            
            domain_motivs = np.sum(domain_motivs,axis=0)
            motiv_insertions = np.sum(motiv_insertions,axis=0)
            
            random_chance = poisson_binomial(domain_motivs,motiv_insertions,variables.chance_motif_tn) #/ (1/sum(domain_motivs))

            significant.append([total_insertions] + [random_chance] + [basket[key].contig] + \
                               [basket[key].identity] + [basket[key].product] + [sum(domain_motivs)] + [ratio_orientation] + \
                               [orient_pvalue] + [domain_part] + [orientation] + [name])
                
            pvalues_list.append(random_chance)   

        else:
            
            sub_domain_cluster, sub_insertions_cluster,domain_part = [], [], []
            subdomain_insert_orient_neg_cluster, subdomain_insert_orient_pos_cluster = 0,0
            insertions = np.append(insertions,1) #avoid overflow
            
            for i, (domain_insert,sub_domain,sub_insertions, sub_name, neg, pos) \
                in enumerate(zip(insertions, domain_motivs, motiv_insertions, \
                    domains, basket[key].subdomain_insert_orient_neg.values(), \
                    basket[key].subdomain_insert_orient_plus.values())):

                subdomain_insert_orient_neg_cluster += neg
                subdomain_insert_orient_pos_cluster += pos
                sub_domain_cluster.append(sub_domain)
                sub_insertions_cluster.append(sub_insertions)
                
                # if there is only one domains in the gene
                if sum(sub_domain) == basket[key].length:

                    ratio_orientation,orient_pvalue,pvalue_orient_list = \
                    ratio_insertions(variables.positive_strand_tn_ratio, subdomain_insert_orient_neg_cluster, subdomain_insert_orient_pos_cluster, pvalue_orient_list)

                    random_chance = poisson_binomial(sub_domain,sub_insertions,variables.chance_motif_tn) #/ (1/sum(sub_domain))
                    
                    significant.append([sum(sub_insertions)] + [random_chance] + [basket[key].contig] + \
                                        [basket[key].identity] + [basket[key].product] + [sum(sub_domain)] + [ratio_orientation] + \
                                        [orient_pvalue] + ["whole gene"] + [orientation] + [name])
                    
                    pvalues_list.append(random_chance) 
                    break

                #if basket[key].domains[-1]==sub_name:
                #    break

                #if the domain is the last in the gene.
                if i==len(domains)-1:

                    sub_domain_cluster = np.sum(sub_domain_cluster,axis=0)
                    sub_insertions_cluster = np.sum(sub_insertions_cluster,axis=0)
                    
                    ratio_orientation,orient_pvalue,pvalue_orient_list = \
                    ratio_insertions(variables.positive_strand_tn_ratio, subdomain_insert_orient_neg_cluster, subdomain_insert_orient_pos_cluster, pvalue_orient_list)

                    random_chance = poisson_binomial(sub_domain_cluster,sub_insertions_cluster,variables.chance_motif_tn) #/ (1/sum(sub_domain_cluster))

                    significant.append([sum(sub_insertions_cluster)] + [random_chance] + [basket[key].contig] + \
                                        [basket[key].identity] + [basket[key].product] + [sum(sub_domain_cluster)] + [ratio_orientation] + \
                                        [orient_pvalue] + [str(domain_part[0]-start) + " to " + str(domains[-1]-start)] + [orientation] + [name])
                    
                    pvalues_list.append(random_chance)  
                
                #if the next domain is basically a continuation of the last (also with/out insertions), and it isnt the last domain of the gene
                elif (((domain_insert == 0) & (insertions[i+1] == 0)) or \
                      ((domain_insert != 0) & (insertions[i+1] != 0))) and (i<len(domains)-1):
                    domain_part.append(sub_name)
                
                #if the next domain is different from the previous(domain appending consideration will break), and also not the last domain in the gene
                elif (((domain_insert == 0) & (insertions[i+1] != 0)) or \
                    ((domain_insert != 0) & (insertions[i+1] == 0))) and (i<len(domains)-1):

                    domain_part.append(sub_name)
    
                    sub_domain_cluster = np.sum(sub_domain_cluster,axis=0)
                    sub_insertions_cluster = np.sum(sub_insertions_cluster,axis=0)
                    
                    ratio_orientation,orient_pvalue,pvalue_orient_list = \
                    ratio_insertions(variables.positive_strand_tn_ratio, subdomain_insert_orient_neg_cluster, subdomain_insert_orient_pos_cluster, pvalue_orient_list)

                    random_chance = poisson_binomial(sub_domain_cluster,sub_insertions_cluster,variables.chance_motif_tn) #/ (1/sum(sub_domain_cluster))
                    
                    significant.append([sum(sub_insertions_cluster)] + [random_chance] + [basket[key].contig] + \
                                        [basket[key].identity] + [basket[key].product] + [sum(sub_domain_cluster)] + [ratio_orientation] + \
                                        [orient_pvalue] + [str(domain_part[0]-start) + " to " + str(domains[i+1]-start)] + [orientation] + [name])
                    
                    pvalues_list.append(random_chance)
                    
                    domain_part = [domains[i+1]]
                    sub_domain_cluster, sub_insertions_cluster = [], []
                    subdomain_insert_orient_neg_cluster, subdomain_insert_orient_pos_cluster = 0,0
                    
                if domain_part[0]-start == domains[-1]-start:
                    break

    return significant,pvalues_list,pvalue_orient_list

def ratio_insertions(p, subdomain_insert_orient_neg_cluster, subdomain_insert_orient_pos_cluster, pvalue_orient_list):

    total_orientation = subdomain_insert_orient_pos_cluster + subdomain_insert_orient_neg_cluster
    
    if total_orientation != 0:
        ratio_orientation = subdomain_insert_orient_pos_cluster / total_orientation #zero means no neg insertions, only positive
        pvalue = binom_test(subdomain_insert_orient_pos_cluster, total_orientation, p, alternative='two-sided')
        pvalue_orient_list.append(pvalue)
        
    else: 
        ratio_orientation, pvalue = "N/A", "N/A"
        
    return ratio_orientation, pvalue, pvalue_orient_list

def pvaluing(basket, significant,pvalues_list,pvalue,variables):
    
    all_genes_list = []
    strain_existent_essentials = set()
    strain_existent_nonessentials = set()
    rejected_baseline_essentials = set()
    rejected_baseline_nonessentials = set()
    remove_signal = 0
    
    baseline_essentials_master = set()
    with open(variables.true_positives) as current:
        for line in current:
            baseline_essentials_master.add(line[:-1])
    
    baseline_non_essentials_master = set()
    with open(variables.true_negatives) as current:
        for line in current:
            baseline_non_essentials_master.add(line[:-1])
    
    fdr = statsmodels.stats.multitest.multipletests(pvalues_list, pvalue, "fdr_bh") #multitest correction, fdr_bh

    ##### getting the essentials
    baseline_essentials,baseline_non_essentials=baseline_essentials_master.copy(),baseline_non_essentials_master.copy()
    for genes, pvalues in zip(significant, fdr[0]):
        #baseline_essentials,baseline_non_essentials=baseline_essentials_master.copy(),baseline_non_essentials_master.copy()
        all_genes_list.append(genes + ["Non-Essential"]) #list that will append all the genes, significant or not
        name = genes[-1]
        identity = genes[3]
        insertions = genes[0]
        domain_lenght = genes[5]
        domain_class = genes[-3]
        gene_half_size = basket[identity].length * 0.5 # 0.4

        if pvalues: #only appends pvalues that are significant
            
            if domain_class == "whole gene":
                all_genes_list[-1] = genes + ["Essential"]
                
            elif domain_lenght >= gene_half_size:
                all_genes_list[-1] = genes + ["Likelly Essential"]
                
            elif domain_lenght < gene_half_size:
                all_genes_list[-1] = genes + ["Possibly Essential"]

        if (insertions == 0) & (all_genes_list[-1][-1] == "Non-Essential"):
            
            if (genes[1] >= fdr[-1]):# & (n > domain): #if the domain is too small for significance @ zero insertions
                remove_signal = 1
                all_genes_list[-1] = genes + ["too small for assaying"]

                if (name in baseline_essentials) & (len(baseline_essentials) >= 30):
                    baseline_essentials.remove(name)
                    
                elif (name in baseline_non_essentials) & (len(baseline_non_essentials) >= 30):
                    baseline_non_essentials.remove(name)

        if remove_signal == 0: #avoids counting genes that cannot be statistically acessed
            
            if (name in baseline_essentials) & (name not in strain_existent_essentials):
                strain_existent_essentials.add(name)
                
                if (pvalues == False) & (name not in rejected_baseline_essentials):
                    rejected_baseline_essentials.add(name)
                
            if (name in baseline_non_essentials) & (name not in strain_existent_nonessentials):  
                strain_existent_nonessentials.add(name)
                
                if (pvalues == True) & (name not in rejected_baseline_nonessentials):
                    rejected_baseline_nonessentials.add(name)
        
        remove_signal = 0
        
    all_genes_list.insert(0, ["#Total Tn insertions"] + ["Essentiality p-value"] + \
                              ["Contig"] + ["Gene ID"] + ["Description"] + ["Domain length"] + \
                                ["Insertion Orientation ratio (+/total)"] + ["Insertion Orientation p-value"] + \
                                ["Domain part"] + ["Gene Orientation"] + ["Gene name"] + ["Essentiality"])

    return [all_genes_list, strain_existent_essentials, fdr[3], rejected_baseline_essentials, rejected_baseline_nonessentials, strain_existent_nonessentials]


def insertions_parser():
    border=[]
    unique_insert = set()
    orient_pos = 0
    with open(variables.insertion_file_path) as current:
        for line in current:
            if "#" not in line:
                skip = False
                line=line.split(",")
                contig = line[0]
                border.append(line[3][:2])
                local = int(line[1])
                
                if len(variables.genome_seq)>1:
                    if local>=len(variables.genome_seq[contig]):
                        skip = True # insertion starts at an unkonwn contig position, skipping
                #larger than len genome insertion are insertions that map to the begining of the genome
                else:
                    local = local - variables.genome_length
                
                insert_ID=line[0]+line[1]+line[2]
                
                if (not skip) and (insert_ID not in unique_insert):
                    if variables.insertions_contig[contig] == {}:
                        variables.borders_contig[contig]=[line[3][:2]]
                        variables.orientation_contig[contig]=[line[2]]
                        variables.insertions_contig[contig]=[local]
                        
                    else:
                        variables.borders_contig[contig].append(line[3][:2])
                        variables.orientation_contig[contig].append(line[2])
                        variables.insertions_contig[contig].append(local)
                    
                    if line[2] == '+':
                        orient_pos += 1
                        
                    unique_insert.add(insert_ID)

    variables.total_insertions=len(unique_insert)
        
    print(f"Total Insertions in library: {variables.total_insertions}")
    #### determine insertion bias by analising at transposon insertion sites in dual bp positions

    variables.positive_strand_tn_ratio = orient_pos / variables.total_insertions
    
    variables.transposon_motiv_count = motiv_compiler(border,variables.regex_compile)
    total = sum(variables.transposon_motiv_count)
    
    variables.transposon_motiv_freq=np.zeros(len(variables.transposon_motiv_count))
    for i,element in enumerate(variables.transposon_motiv_count):
        if element != 0:
            variables.transposon_motiv_freq[i] = round(element / total * 100,1) 
            
    variables.chance_motif_tn = variables.normalizer() #calculating the insertion frequency

    print("Transposon insertion frequency (on leading strand):")
    for tn,mtv in zip(variables.transposon_motiv_freq, variables.di_motivs):
        print("{}: {}%".format(mtv,tn))

def basket_storage():
    print("Parsing Gene information...")
    file = variables.annotation_file_paths[0]
    
    if variables.annotation_type == "gff":
        return gene_info_parser_gff(file)
    
    elif variables.annotation_type == "gb":
        return gene_info_parser_genbank(file)

def cpu():
    c = multiprocessing.cpu_count()
    if c >= 2:
        c -= 1  
    pool = multiprocessing.Pool(processes = c)
    return pool, c

def insertion_annotater(chunk,variables):
    for key in chunk:
        subdomain_insertions,subdomain_insert_seq = {}, {}
        
        GC_content,domains=[],[]
        for i, subdomain in enumerate(chunk[key].domains[:-1]): #first element is start position of gene
            GC_content.append(np.array(count_GC([variables.genome_seq[chunk[key].contig][subdomain:chunk[key].domains[i+1]+1]],\
                                                variables.regex_compile)))
            domains.append(subdomain)
            subdomain_insert_seq[subdomain] = [""]#every domain needs an entry, even if empty
            chunk[key].subdomain_insert_orient_plus[subdomain] = 0
            chunk[key].subdomain_insert_orient_neg[subdomain] = 0
        
        chunk[key].domain_notes=domains
        chunk[key].GC_content=GC_content
        #### pinning all the insertions to their gene domains

        for i, subdomain in enumerate(chunk[key].domains[:-2]):
            domain_start=subdomain-chunk[key].start
            domain_end=chunk[key].domains[i+1]-chunk[key].start
            subdomain_insertions[subdomain] = sum(chunk[key].gene_insert_matrix[domain_start:domain_end])
            if subdomain_insertions[subdomain] != 0:
                for j in range(subdomain-1,chunk[key].domains[i+1]-1): 
                    border = variables.borders_contig[chunk[key].contig][j]
                    insert = variables.insertions_contig[chunk[key].contig][j]
                    if insert==1:
                        subdomain_insert_seq[subdomain] = subdomain_insert_seq[subdomain] + [border]
                        if variables.orientation_contig_plus[chunk[key].contig][j] == 1: #positive insertion
                            chunk[key].subdomain_insert_orient_plus[subdomain] += 1
                        if variables.orientation_contig_neg[chunk[key].contig][j] == 1: #negative insertion
                            chunk[key].subdomain_insert_orient_neg[subdomain] += 1

        ### Transposon motif content in each domain (alwyas 16, corresponding to the dinucleotide combo)
        if subdomain_insert_seq != {}:
            motif_seq=[]
            for key1,value in sorted(subdomain_insert_seq.items()): 
                motif_seq.append(motiv_compiler(value,variables.regex_compile))
            chunk[key].motif_seq = motif_seq
            
        else:
            chunk[key].motif_seq=np.zeros(16)
        
        chunk[key].domain_insertions_total=np.array(([]),dtype=int)
        for key1,value in sorted(subdomain_insertions.items()):
            chunk[key].domain_insertions_total=np.concatenate((chunk[key].domain_insertions_total,[value]))
            
    significant,pvalues_list,pvalue_orient_list=essentials(chunk,variables)

    return significant,pvalues_list,pvalue_orient_list,chunk

def multi_annotater(basket):
    pool, cpus = cpu()
    # divides the dictionary keys into smaller blocks that can be efficiently be multiprocessed
    divider=len(basket)//cpus
    return_list = [dict() for i in range(cpus)]
    i,list_iter=0,0
    for k in basket:
        if i<cpus:
            return_list[i][k]=basket[k]
        
        if i == cpus: #odd number split will be distributed equally 
            list_iter+=1
            return_list[list_iter][k]=basket[k]
                
        elif len(return_list[i]) >= divider:
            i+=1

    result_objs = []
    for chunk in return_list:
        result = pool.apply_async(insertion_annotater, args=((chunk,variables)))
        result_objs.append(result)

    pool.close()
    pool.join()

    result = [result.get() for result in result_objs]
    #demultiplexing the results
    essentials,pvalues,pvalues_orient=[],[],[]
    for subresult in result:
        for essential in subresult[0]:
            essentials.append(essential)
        for pvalue in subresult[1]:
            pvalues.append(pvalue)
        for pvalue_orient in subresult[2]:
            pvalues_orient.append(pvalue_orient)
        for key in basket:
            if key in subresult[3]:
                basket[key] = subresult[3][key]

    return essentials,pvalues,pvalues_orient,basket

def pvalue_iteration(basket,significant,pvalues_list,pvalue,pvalue_listing,euclidean_points,variables):
    essential_list, strain_existent_essentials, fdr, rejected_baseline_essentials, \
    rejected_baseline_nonessentials, strain_existent_nonessentials = pvaluing(basket, significant,pvalues_list, pvalue,variables)
                
    if len(essential_list) == 1: #if there is only the header
        rejected_baseline_essentials = strain_existent_essentials
    
    if len(strain_existent_essentials) > 0:
        
        TP = len(strain_existent_essentials) - len(rejected_baseline_essentials)
        FN = len(rejected_baseline_essentials)

        if (TP + FN) != 0:
            TPR_sensitivity = TP / float(TP + FN)
        else:
            TPR_sensitivity = 0

        TN = len(strain_existent_nonessentials) - len(rejected_baseline_nonessentials)
        FP = len(rejected_baseline_nonessentials)
        
        if (TN + FP) != 0:
            specificity = 1 - (TN / float(TN + FP))
        else:
            specificity = 0
        
    else:
        TPR_sensitivity = 0
        specificity = 0
        print("There are no known Benchmark essential genes in this strain")
        
    pvalue_listing.append(pvalue)
    euclidean_points.append([specificity] + [TPR_sensitivity])
    #print("TPR = {}, TNR = {}, p-value threshold = {}".format(euclidean_points[-1][1],euclidean_points[-1][0], pvalue))
    
    return pvalue_listing, euclidean_points

def multi_pvalue_iter(basket,significant,pvalues_list):
    pvalue=variables.pvalue
    pvalue_listing, euclidean_points,result_objs = [],[],[]
    iterator = 1
    temp_basket = basket.copy()
    while iterator>0:
        
        pool, cpus = cpu()
        subdivied = []
        for i in range(cpus):
            subdivied.append(pvalue)
            pvalue *= 0.8
            
        for p in subdivied:
            result=pool.apply_async(pvalue_iteration, args=((temp_basket,significant,pvalues_list,p,pvalue_listing,euclidean_points,variables)))
            result_objs.append(result)
        pool.close()
        pool.join()        
        result = [result.get() for result in result_objs]
        result = sorted(result, key=lambda e: e, reverse=True)
        iterator = round(sum(result[-1][-1][-1]),1)

    result = [result.get() for result in result_objs]
    result = sorted(result, key=lambda e: e, reverse=True)
    pvalue_listing, euclidean_points = zip(*result)
    pvalue_listing=[n[0] for n in pvalue_listing]
    euclidean_points=[n[0] for n in euclidean_points]
    
    return pvalue_listing, euclidean_points

def final_compiler(basket,significant,pvalues_list,pvalue,euclidean_points):

    essential_list = pvaluing(basket,significant,pvalues_list,pvalue,variables)
    legenda = pvalue
    
    genes_list = essential_list[0][1:]
    fdr = essential_list[2]

    significant_genes_list = list(filter(lambda x: x[-1] == "Essential", genes_list)) #gets just the essentials
    significant_genes_list_full = significant_genes_list + list(filter(lambda x: x[-1] == "Likelly Essential", genes_list)) #gets just the essentials
    significant_genes_list_full = significant_genes_list_full + list(filter(lambda x: x[-1] == "Possibly Essential", genes_list)) #gets just the essentials
    non_assayed = list(filter(lambda x: x[-1] == "too small for assaying", genes_list)) #gets just the non evaluated genes
    non_essentials = list(filter(lambda x: x[-1] == "Non-Essential", genes_list)) #gets just the non essentials
    
    essentials = set()
    a=[essentials.add(gene[-2]) for gene in significant_genes_list_full]
    
    non_assayed_list = set()
    a=[non_assayed_list.add(gene[-2]) for gene in non_assayed if gene[-2] not in non_assayed_list]
    
    non_essentials_list = set()
    a=[non_essentials_list.add(gene[-2]) for gene in non_essentials if gene[-2] not in non_essentials_list]
    
    intersect=non_assayed_list.intersection(essentials)
    intersect |= non_assayed_list.intersection(non_essentials_list)
    full_na_genes = len(non_assayed_list) - len(intersect)
    intersect=non_essentials_list.intersection(essentials)
    intersect |= non_essentials_list.intersection(non_assayed_list)
    full_non_e_genes = len(non_essentials_list) - len(intersect)
    
    dic={}
    for x,i in zip(variables.transposon_motiv_freq, variables.di_motivs):
        dic[i] = x
    
    genes_list.insert(0, ["#Transposon insertion percent bias (+strand): %s" % dic]) 
    genes_list.insert(0, ["#p-value cutoff: %s" % pvalue]) 
    genes_list.insert(0, ["#fdr corrected p-value cutoff: %s" % fdr]) 
    genes_list.insert(0, ["#Number of genes with at least one domain that is non-essential: %s" % len(non_essentials_list)])   
    genes_list.insert(0, ["#Number of whole genes that are non-essential: %s" % full_non_e_genes]) 
    genes_list.insert(0, ["#Number of genes with at least one domain too small for assaying: %s" % len(non_assayed_list)]) 
    genes_list.insert(0, ["#Number of whole genes too small for assaying: %s" % full_na_genes]) 
    genes_list.insert(0, ["#Number of genes with at least one domain that is essential: %s" % len(essentials)])  
    genes_list.insert(0, ["#Number of whole genes that are essential: %s" % len(significant_genes_list)]) 
                                      
    output_writer(variables.directory, variables.output_name, genes_list)                                  

    fig, ax1 = plt.subplots()  
         
    plt.xlim(0, 1)
    plt.ylim(0, 1)
        
    ax1.set_xlabel("True Negative Rate") #1 - specificity
    ax1.set_ylabel("True Positive Rate") #(sensitivity)
    ax1.plot(*zip(*euclidean_points), color = "midnightblue")
            
    ax1.plot(ax1.get_xlim(), ax1.get_ylim(), ls="--", c=".3")
    ax1.tick_params(axis='y')
    ax1.set_title("Reciver Operator Curve (ROC)\nused to auto-determine the essentiality calling threshold for %s" % variables.strain, size = 9, pad = 13)
    ax1.legend([legenda], loc="lower right")
    
    fig.tight_layout()
        
    plt.savefig(f"{variables.directory}/ROC_curves{variables.strain}.png", dpi=300)
    
    return
    
def genome_loader():

    if variables.annotation_type == "gff":
        with open(variables.annotation_file_paths[1]) as current:
            for line in current:
                if ">" in line:     
                    contig = line.split()[0][1:]
                    variables.genome_seq[contig] = ""
                    variables.borders_contig[contig]={}
                    variables.orientation_contig[contig]={}
                    variables.insertions_contig[contig]={}
                else:
                    variables.genome_seq[contig]+=line[:-1]
                    
        for contig in variables.genome_seq:
            print(f"Loaded: {contig}")
            variables.genome_length += len(variables.genome_seq[contig])
        
    elif variables.annotation_type == "gb":
        for rec in SeqIO.parse(variables.annotation_file_paths[0], "gb"):
            variables.genome_length = len(rec.seq)
            variables.annotation_contig = rec.id
            variables.borders_contig[variables.annotation_contig]={}
            variables.orientation_contig[variables.annotation_contig]={}
            variables.insertions_contig[variables.annotation_contig]={}
            print(f"Loaded: {variables.annotation_contig}")
            variables.genome_seq[variables.annotation_contig] = str(rec.seq)
            
def domain_iterator(basket):
    
    def ROC(basket, significant, pvalues_list,pvalues_orient):

        def orientation_pvaluing(pvalues_orient, significant):
            if len(pvalues_orient) > 0:
                fdr = statsmodels.stats.multitest.multipletests(pvalues_orient, 0.01, "fdr_bh") #multitest correction, fdr_bh
            p = 0
            for i, entry in enumerate(significant):
                if entry[-4] != "N/A":
                    significant[i][-4] = fdr[1][p]
                    p += 1
            return significant
    
        significant=orientation_pvaluing(pvalues_orient, significant)
        store = multi_pvalue_iter(basket,significant,pvalues_list)
    
        pvalue_listing, euclidean_points = store[0], store[1]
    
        output_writer(variables.directory, "ROC_points{}".format(variables.output_name), euclidean_points)

        convergence = [[0] + [1]] * len(euclidean_points) #point where TPR_sensitivity = 1 and 1-specificity = 0
    
        #lower is better
        distances = scipy.spatial.distance.cdist(np.array(euclidean_points),np.array(convergence),'euclidean')
        
        optimal_distance = []
        list(filter(lambda x: optimal_distance.append(x[0]), distances)) #returns first entry of the array of ecludian
        inflexion_points_index = (optimal_distance.index(min(optimal_distance))) #gives the index of the inflexion point. that minimizes the eucledian distances
    
        pvalue = pvalue_listing[inflexion_points_index]
        best_distance = optimal_distance[inflexion_points_index]
    
        return pvalue, best_distance, euclidean_points
    
    def iterating(i,iterator_store,euclidean_distances,pvalues_list_list,significant_list,basket_list,basket):
        basket=domain_resizer(variables.domain_iteration[i],basket)
        significant,pvalues_list,pvalues_orient,basket = multi_annotater(basket)
        significant_list.append(significant)
        pvalues_list_list.append(pvalues_list)
        basket_list.append(basket)
        best_pvalue, best_distance, euclidean_points = ROC(basket, significant, pvalues_list,pvalues_orient)
        euclidean_distances.append(euclidean_points)
        iterator_store.append([variables.domain_iteration[i]] + [best_pvalue] + [best_distance]+[i])
        return iterator_store, euclidean_distances,pvalues_list_list,significant_list,basket_list
    
    biggest_gene=0
    for gene in basket:
        current = basket[gene].length
        if current > biggest_gene:
            biggest_gene = current
    
    euclidean_distances = []
    iterator_store = [[10,0],[9,0]] #Mock data, will be eliminated later
    significant,pvalues_list,previous_basket= [],[],[]
    i,current_gap = 0,0

    while (i<len(variables.domain_iteration)) and (current_gap<=biggest_gene): 
        current_gap = int(variables.genome_length / variables.total_insertions * variables.domain_iteration[i])
        print(f"Current Domain divider size: {current_gap}bp")
        iterator_store,euclidean_distances,pvalues_list,significant,previous_basket = iterating(i,iterator_store,euclidean_distances,pvalues_list,significant,previous_basket,basket)
        i += 1
        
    del iterator_store[:2]
    sorted_optimal=sorted(iterator_store, key=lambda e:e[2])
    variables.best_domain_size = sorted_optimal[0][0]
    print(f"Optimal domain division size: {int(variables.genome_length / variables.total_insertions * variables.best_domain_size)}bp")
    fig, ax1 = plt.subplots()  
         
    plt.xlim(0, 1)
    plt.ylim(0, 1)
        
    ax1.set_xlabel("True Negative Rate") #1 - specificity
    ax1.set_ylabel("True Positive Rate") #(sensitivity)
    
    legenda = []
    
    for euclid, size in zip(euclidean_distances, iterator_store):
        ax1.plot(*zip(*euclid))
        legenda.append(size[0])
            
    ax1.plot(ax1.get_xlim(), ax1.get_ylim(), ls="--", c=".3")
    ax1.tick_params(axis='y')
    ax1.set_title("Reciver Operator Curve (ROC)\nused to auto-determine the essentiality calling threshold for %s" % variables.strain, size = 9, pad = 13)
    ax1.legend(legenda, loc="lower right")
    
    fig.tight_layout()
    plt.savefig(variables.directory + "\ROC_curves_iterator_%s" % variables.strain + ".png", dpi=300)
    
    best_index = int(sorted_optimal[0][-1])
    return significant[best_index],pvalues_list[best_index],previous_basket[best_index],iterator_store[best_index][1],euclidean_distances[best_index]

def main(argv):
    
    print(f"\nStarting at: {datetime.datetime.now().strftime('%c')}")
    inputs(argv)
    path_finder() 
    genome_loader()
    insertions_parser()
    basket=basket_storage()
    basket=gene_insertion_matrix(basket) #maps insertions to the genome
    significant,pvalues_list,best_basket,pvalue,euclidean_points = domain_iterator(basket)
    final_compiler(best_basket,significant,pvalues_list,pvalue,euclidean_points)
    print(f"Ended on: {datetime.datetime.now().strftime('%c')}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        argv = sys.argv[1:]
    main(argv)