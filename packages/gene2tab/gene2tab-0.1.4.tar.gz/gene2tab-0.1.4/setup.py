from setuptools import setup, find_packages
import codecs

setup(
    name="gene2tab",
    install_requires=[
        "tabulate",
        "pandas",
    ],
    version="0.1.4",
    author="Iker García-Ferrero",
    author_email="igarciaf896@gmail.com",
    license="Apache License 2.0",
    description="Creates a table with the presence/absence of genes in samples",
    long_description=codecs.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "gene2tab=src.gene2tab:main",
        ],
    },
    url="https://github.com/ikergarcia1996/Gene2Tab",
)
