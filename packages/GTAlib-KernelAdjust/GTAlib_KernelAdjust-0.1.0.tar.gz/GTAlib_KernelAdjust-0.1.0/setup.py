from setuptools import find_packages, setup

with open('README.md','r') as fh:
    description_l = fh.read()


setup(
    name = 'GTAlib_KernelAdjust',
    version = '0.1.0',
    packages = find_packages(include = ['GTAlib_KernelAdjust']),
    description='Libreria para el ajuste de datos utilizando distintos kernels',
    long_description = description_l,
    long_description_content_type = 'text/markdown',
    author='German',
    license = 'MIT',
    install_requires = ['numpy==1.26.1','pandas==2.1.2','matplotlib==3.8.1'],
    python_requires = '>=3.11.6',
    author_email = 'german.torres@udea.edu.co',
    url = 'https://gitlab.com/gtorresa312/trabajos-en-clase.git'
    
)