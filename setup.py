# The setup.py file is used to define this project as a Python package. 
# It allows tools like pip to install the package and its dependencies,
# and makes it possible to use the codebase in other projects or development environments.

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []
    
    try:
        # Open and read the requirements.txt file
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                # Strip whitespace and newline characters
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    
        
    return requirement_list
print(get_requirements())
setup(
    name="document_portal",
    author="Artur Dragunov",
    version="0.1",
    packages=find_packages(), # whichever folder has __init__.py inside, will be considered as a module for the project package.
    install_requires=get_requirements()
)
