from setuptools import find_packages, setup
def get_requirements(file_path):
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
    requirements=[req.replace('\n',"") for req in requirements]
    return requirements[:-1]

setup(
name='mlproject',
version='0.0.1',
author='',
author_email='@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)