# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='src',
    version='1.0',
    description='Source code for my project',
    long_description=readme,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Topic :: Anomaly Detection :: Machine Learning',
    ],
    author='Tzu-Hua Kao',
    author_email='tzu-hua.kao@campus.tu-berlin.de',
    url='https://github.com/KaoCircle/anomalyDetection',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),  # same as name
    # install_requires=['bar', 'greek'], #external packages as dependencies
    # scripts=[
    #         'scripts/cool',
    #         'scripts/skype',
    #        ]
    # ref:https://stackoverflow.com/questions/1471994/what-is-setup-py
)
