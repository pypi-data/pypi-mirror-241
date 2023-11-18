from setuptools import setup, find_packages

setup(
    name='CharPackage',
    version='0.1',
    author='James Evans',
    author_email='Joesaysahoy@gmail.com',
    packages=find_packages(),
    requires=['CharActor', 'CharObj', 'CharTask']
)