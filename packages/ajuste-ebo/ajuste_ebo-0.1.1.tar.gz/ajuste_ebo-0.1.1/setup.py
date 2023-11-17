from setuptools import find_packages, setup


with open("README.md" , "r") as fh:
    description_l = fh.read()
setup(
    name="ajuste_ebo",
    version="0.1.1",
    packages=find_packages(include=["ajuste_ebo"]),
    description="Libreria para realizar ajustes de curva con 3 tipos de \
        kernels, gaussiano, tricube , Epanechnikov",
    long_description=description_l,
    long_description_content_type="text/markdown",
    author=" Emmanuel Botero  ",
    license="MIT",
    install_requires=[ "tqdm==4.66.1" ,"numpy==1.26.1" , "pandas==2.1.2" , "matplotlib==3.8.1"],
    python_requires=">=3.10.12",
    author_email="emmanuel.botero@udea.edu.co"

)