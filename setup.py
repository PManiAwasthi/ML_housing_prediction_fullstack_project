from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "HOUSING-PREDICTOR"
VERSION = "0.0.1"
AUTHOR="PRAKASHMANI AWASTHI"
DESCRIPTION="This is a full stack data science project for predicting house prices using california housing dataset"

REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT="-e ."

def get_requirements_list() -> List[str]:
    """
    Description: This function is made to return the list of requirements
    mentioned in requirements.txt file
    return of this function is a list containing all the libraries
    mentioned in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        requirements_list = requirements_file.readlines()
        requirements_list = [requirement_name.replace("\n", "") for requirement_name in requirements_list]
        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)
        return requirements_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)