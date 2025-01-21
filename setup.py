from setuptools import setup, find_packages
from typing import List


def get_requirements(filename:str)->List[str]:
    '''
    Read the requirements file and return list of requirements
    '''
    HYPEN_E_Dot='-e .' # type: ignore
    requirements=[]
    with open(filename) as file:
        requirements=file.readlines()
        requirements=[requirement.replace("\n",'') for requirement in requirements]

        if HYPEN_E_Dot in requirements: # type: ignore
            requirements.remove(HYPEN_E_Dot) # type: ignore
        return requirements

    
setup(
	name='Studentproject',
	version='0.0.1',
	author='Dhruv',
	author_email='naikdhruv1502@gmail.com',
	packages=find_packages(),
	install_requires=get_requirements('requirements.txt')
)