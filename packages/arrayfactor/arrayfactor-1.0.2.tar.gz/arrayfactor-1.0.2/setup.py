# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 13:35:32 2021

@author: Merve Tascioglu
"""


from setuptools import setup


VERSION = '1.0.2'
DESCRIPTION = 'Array Factor Calculator'

def readme():
    with open('./README.md') as f:
        return f.read()

                                                                                                               
# Setting up
setup(
    name="arrayfactor",
    version=VERSION,
    author="Merve Tascioglu",
    author_email="<merve.tascioglu@barkhauseninstitut.org>",
    description=DESCRIPTION,
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords=['python', 'antenna array', 'array factor'],
    
    classifiers=[
            "Development Status :: 1 - Planning",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
    ],
    packages=['lib'],
    install_requires=[],
    include_package_data=True    
    
)