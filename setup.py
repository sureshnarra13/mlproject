from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function returs the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name='mlproject',                  # Usually lowercase with hyphens if publishing
    version='0.0.1',                   # 0.01 → 0.0.1 is more conventional
    author='Suresh',
    author_email='sureshnarra13@gmail.com',
    packages=find_packages(),          # finds every folder with __init__.py
    install_requires= get_requirements('requirements.txt'),
)

