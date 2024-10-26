import setuptools

setuptools.setup(
    name='func',
    version='1.0.0',
    author='Alexander Cook',
    author_email='alchemerxander@gmail.com',
    description='Bunch of utils',
    long_description='A list of utils i use for every project',
    url='https://github.com/SirAlchemer/func/',
    packages=setuptools.find_packages(),
    install_requires=[
        'dependency1',
        'dependency2',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
