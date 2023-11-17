from setuptools import find_packages, setup

with open('./README.md','r') as fn:
    description_1 = fn.read()

setup(
    name='FdoJarParcial2',
    version='0.1.2',
    packages=find_packages(include=['FdoJarParcial2']),
    description='Suavizado de curvas',
    long_description=description_1,
    long_description_content_type = 'text/markdown',
    author='Fernando Jaramillo',
    license= 'MIT',
    install_requirements=  ['certifi==2023.7.22,'
                            'cffi==1.16.0,'
                            'charset-normalizer==3.3.2,'
                            'contourpy==1.2.0,'
                            'cryptography==41.0.5,'
                            'cycler==0.12.1,'
                            'docutils==0.20.1,'
                            'fonttools==4.44.3,'
                            'idna==3.4,'
                            'importlib-metadata==6.8.0,'
                            'jaraco.classes==3.3.0,'
                            'jeepney==0.8.0,'
                            'keyring==24.3.0,'
                            'kiwisolver==1.4.5,'
                            'markdown-it-py==3.0.0,'
                            'matplotlib==3.8.1,'
                            'mdurl==0.1.2,'
                            'more-itertools==10.1.0,'
                            'nh3==0.2.14,'
                            'numpy==1.26.2,'
                            'packaging==23.2,'
                            'pandas==2.1.3,'
                            'Pillow==10.1.0,'
                            'pkginfo==1.9.6,'
                            'pycparser==2.21,'
                            'Pygments==2.16.1,'
                            'pyparsing==3.1.1,'
                            'python-dateutil==2.8.2,'
                            'pytz==2023.3.post1,'
                            'readme-renderer==42.0,'
                            'requests==2.31.0,'
                            'requests-toolbelt==1.0.0,'
                            'rfc3986==2.0.0,'
                            'rich==13.7.0,'
                            'SecretStorage==3.3.3,'
                            'six==1.16.0,'
                            'twine==4.0.2,'
                            'tzdata==2023.3,'
                            'urllib3==2.1.0,'
                            'zipp==3.17.0,'],
    python_requirements='3.11.4',
    author_email='juanf.jaramillo@udea.edu.co',
    url='https://gitlab.com/juanf.jaramillo1/curso-fci-2023-2.git'
    
)