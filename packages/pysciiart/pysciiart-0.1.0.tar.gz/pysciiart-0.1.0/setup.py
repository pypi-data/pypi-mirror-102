#!/usr/bin/env python3
from setuptools import setup

from src.pysciiart import __version__

setup(
    name='pysciiart',
    version=__version__,
    packages=['pysciiart'],
    package_dir={'pysciiart': './src/pysciiart'},
    test_suite='tests',
    setup_requires=['pytest-runner'],
    install_requires=['termcolor == 1.1.0'],
    tests_require=['pytest'],
    url='https://gitlab.com/alcibiade/pysciiart',
    license='MIT',
    author='Yannick Kirschhoffer',
    author_email='alcibiade@alcibiade.org',
    description='A set of python libraries used to generate ASCII art from high level data structures.',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
