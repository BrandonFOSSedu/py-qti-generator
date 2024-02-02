"""Package configuration"""
from setuptools import find_packages, setup

setup(
    name='PyQTIGenerator',
    version='0.0.1',
    packages=find_packages(),
    author='Brandon Murry',
    author_email='brandonfossedu@gmail.com',
    install_requires=[
        'lxml'
        ]
) 
