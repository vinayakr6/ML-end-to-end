from setuptools import find_packages, setup
from typing import List

hypen_e_dot = '-e .' # written in requirements.txt to execute or connect setup.py

def get_requirements(file_path: str)->List[str]:
    '''Returns a list 
    of requirements'''

    requirements = [] # Empty list created
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if hypen_e_dot in requirements:  # ignoring '-e .' present in requirements.txt
            requirements.remove(hypen_e_dot)

    return requirements    

setup(
    name = "ML End to End Project",
    version = '0.0.1',
    author = "VinayakR",
    author_email = "vinayakr6@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)