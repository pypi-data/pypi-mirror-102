# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 13:35:32 2021

@author: Merve Tascioglu
"""


from setuptools import setup,find_packages


VERSION = '1.0.1'
DESCRIPTION = 'Array Factor Calculator'
README = ('./README.md')                                                                                                               
                                                                                                               

# Setting up
setup(
    name="arrayfactor",
    version=VERSION,
    author="Merve Tascioglu",
    author_email="<merve.tascioglu@barkhauseninstitut.org>",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'antenna array', 'array factor'],
    
    classifiers=[
            "Development Status :: 1 - Planning",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]    
    
)