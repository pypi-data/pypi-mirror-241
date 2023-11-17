from setuptools import find_packages, setup

with open('./README.md','r') as fn:
    description_1 = fn.read()

setup(
    name='FdoJarParcial2',
    version='0.1.3',
    packages=find_packages(include=['FdoJarParcial2']),
    description='Suavizado de curvas',
    long_description=description_1,
    long_description_content_type = 'text/markdown',
    author='Fernando Jaramillo',
    license= 'MIT',
    #install_requirements=  ['numpy'],
    python_requirements='3.11.4',
    author_email='juanf.jaramillo@udea.edu.co',
    url='https://gitlab.com/juanf.jaramillo1/curso-fci-2023-2.git'
    
)