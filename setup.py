from os import name
from setuptools import setup, find_packages, version

setup(
    name="plpred",
    version="0.0.1",
    packages= find_packages(),
    author="Giuli Argou Marques",
    author_email="giulizynhah@gmail.com",
    description= "plpred: a protein subcellular location prediction program",
    keywords="bioinformatics",
    entry_points = {
        'console_scripts': [
            'plpred-preprocess = plpred.preprocessing:main',
            'plpred-train = plpred.training:main',
            'plpred-predict = plpred.prediction:main',
            'plpred-server = plpred.server:main'
        ]
    }
)