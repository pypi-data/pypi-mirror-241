from setuptools import find_packages, setup

setup(
    name='dams_extractor',
    author='Brian Scherzo',
    version='0.2.2',
    description='A boilerpy3 text extractor wrapper',
    long_description='A text extraction tool made for use by the UMBC DAMS Lab.',
    packages=find_packages(),
    zip_safe=False
)