# -*- coding: utf-8 -*-
"""Installer for the melange package."""
from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='melange',
    version='1.0',
    description="a web composer",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Python Plone',
    author='Jens W. Klein',
    author_email='jk@kleinundpartner.at',
    url='http://pypi.python.org/pypi/melange',
    license='BSD',
    packages=find_packages('src'),
    namespace_packages=[],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'lxml',
        'setuptools',
    ],
    extras_require={
        'test': [
            'ipdb',
        ],
    },
    entry_points="""
    """,
)
