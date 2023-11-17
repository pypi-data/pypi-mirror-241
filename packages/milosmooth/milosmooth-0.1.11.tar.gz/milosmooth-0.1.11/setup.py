from setuptools import setup, find_packages

with open("README.md","r") as fh:
    description_l = fh.read()

setup(
    name='milosmooth',
    version='0.1.11',
    packages=find_packages(include=['milosmooth']),
    description='Libreria de suavizado de curvas',
    long_description=description_l,
    long_description_content_type="text/markdown",
    author='Milo',
    license='MIT',
    install_requires=["numpy==1.26.1", "pandas==2.1.2","matplotlib==3.8.1"],
    python_requires='>=3.10.12',
    author_email = "camilo.londonov@udea.edu.co",
    url = "https://gitlab.com/camilo.londonov"

)