from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path : str)->List[str]:
    '''This is get requirement function to creae a package'''

    requirements = []
    with open(file_path) as obj:
        requirements = obj.readline()
        requirements = [req.replace("/n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='ml_project',
    version='0.0.1',
    author='Rahul',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)