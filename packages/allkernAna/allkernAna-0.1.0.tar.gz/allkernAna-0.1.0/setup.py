from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    description_l= fh.read()

setup(
    name='allkernAna',
    version='0.1.0',
    packages=find_packages(include= ['allkernAna']),
    description='libreria de suavizado con kernell gausiano, tricube y Epanechikov',
    long_description=description_l,
    long_description_content_type='text/markdown',
    author='Ana Maria',
    license='MIT',
    install_requires=['cycler==0.11.0', 'fonttools==4.38.0', 'kiwisolver==1.4.5', 'matplotlib==3.5.3', 'numpy==1.21.6', 'packaging==23.2', 'pandas==1.3.5', 'Pillow==9.5.0', 'pyparsing==3.1.1', 'python-dateutil==2.8.2', 'pytz==2023.3.post1', 'six==1.16.0', 'typing_extensions==4.7.1'],
    python_requires='>=3.7.2',
    author_email='aarcila01@gmail.com',
    git= 'https://gitlab.com/ana.arcila1/cursofci-2023-2.git'

)