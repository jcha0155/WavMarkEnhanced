from setuptools import setup, find_packages

setup(
    name='MDS07Watermark',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',  # Example dependency
        'soundfile',
        'torch'
    ],
    author='Jian Sen Chan',
    author_email='jcha0155@student.monash.edu',
    description='FIT3164 MDS07',
    url='https://github.com/jcha0155/WavMarkEnhanced.git',
    license='Jian Sen',
)