from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements_lst: List[str] = []
    try:
        with open(file_path , 'r') as file_obj:
            lines = file_obj.readlines()
            requirements_lst = [line.strip() for line in lines]
            if HYPEN_E_DOT in requirements_lst:
                requirements_lst.remove(HYPEN_E_DOT)
        return requirements_lst
    except FileNotFoundError:
        print("requirements.txt file not found.")
    



setup(
    name='NetworkSecurity',
    version='0.1.0',
    packages=find_packages(),
    author='Sohanur Rahman',
    author_email='sohanurrahmansohan238@gmail.com',
    install_requires=get_requirements('requirements.txt')
)