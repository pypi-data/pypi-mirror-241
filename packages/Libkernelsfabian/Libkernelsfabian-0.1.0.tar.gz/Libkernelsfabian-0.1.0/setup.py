from setuptools import find_packages, setup

with open("README.md","r") as fh:
    description_l=fh.read()

setup(
    name="Libkernelsfabian",
    version='0.1.0',
    packages=find_packages(include=["kernelsfabian"]),  #nombre con el que vamos a importar la librería, es el nombre de la carpeta donde está contenido el __init__.py
    description="diferentes suavizados en esta librería",
    long_description=description_l,
    long_description_content_type="text/markdown",
    author="Fabian",
    license="MIT",
    install_requires=["numpy==1.26.2","pandas==2.1.3","matplotlib==3.8.1"],
    python_requires=">=3.10.12",
    author_email="fyamith.tovar@udea.edu.co"
)