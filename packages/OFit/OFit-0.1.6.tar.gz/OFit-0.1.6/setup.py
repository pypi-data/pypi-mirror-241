from setuptools import setup, find_packages

with open("README.md","r") as fh:
    description_l = fh.read()

setup(
    name='OFit',
    version='0.1.6',
    packages=find_packages(include=['Ofit']),
    description='Esta libreria se encarga de realizar el analisis de datos usando un kernel gaussiano, trucube y Epanechnikov',
    long_description=description_l,
    long_description_content_type="text/markdown",
    author='Juan Esteban Ospina ',
    license='MIT',
    install_requires=["numpy==1.26.1","pandas==2.1.1","matplotlib==3.8.0"],
    python_requires='>=3.10.12',
    author_email = "juan.ospina25@udea.edu.co"

)