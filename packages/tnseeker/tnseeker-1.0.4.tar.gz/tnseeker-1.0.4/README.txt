on anaconda/ubuntu:
pip install "/mnt/d/UNIL/Python Programs/crispery/base-crispery/dist/crispery-1.4.4-py3-none-any.whl"

To upload to PyPI:
on windows powersheel (on correct directory):
python setup.py sdist bdist_wheel
twine upload dist/*
username: afombravo