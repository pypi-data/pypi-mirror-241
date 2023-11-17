#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages, Extension

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Meinolf Sellmann",
    author_email='info@insideopt.com',
#    python_requires='==3.10',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
        'Operating System :: POSIX :: Linux'
    ],
    description="InsideOpt Seeker Demo Distribution",
    install_requires=requirements,
    long_description=readme, 
    keywords='insideopt, seeker, demo, optimization',
    name='insideopt-demo',
    test_suite='tests',
    version='0.0.13',
    packages=find_packages(include=['seekerdemo', 'seekerdemo.*', '*.so']),
    package_data={'seekerdemo': ['*.so', 'seekerdemo.py']},
    zip_safe=False,
)
