from setuptools import find_packages ,setup
from typing import List

def get_requirements()->List[str]:
    """
    Thiss function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="Security",
    version="0.0.1",
    author="Nandi",
    author_email="nandhivardhan171@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)