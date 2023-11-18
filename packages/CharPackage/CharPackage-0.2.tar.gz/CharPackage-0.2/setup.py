from setuptools import setup, find_packages

setup(
    name='CharPackage',
    version='0.2',
    author='James Evans',
    author_email='Joesaysahoy@gmail.com',
    packages=find_packages(),
    install_requires=['CharActor', 'CharObj', 'CharTask']
)