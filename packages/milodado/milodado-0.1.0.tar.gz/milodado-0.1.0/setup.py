from setuptools import setup, find_packages

with open("README.md","r") as fh:
    description_l = fh.read()

setup(
    name='milodado',
    version='0.1.0',
    packages=find_packages(include=['milodado']),
    description='Libreria de probabilidad de dados',
    long_description=description_l,
    long_description_content_type="text/markdown",
    author='Milo',
    license='MIT',
    install_requires=["numpy==1.26.1", "matplotlib==3.8.1"],
    python_requires='>=3.10.12',
    author_email = "camilo.londonov@udea.edu.co",
    url = "https://gitlab.com/camilo.londonov"

)