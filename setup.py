#!/usr/bin/env python3
from setuptools import find_packages, setup

# with open('README.rst') as f:
#     readme = f.read()

setup(
    name='pgapi',
    version='0.0.1',
    license='MIT',
    author='Adrian Vondendriesch',
    author_email='adrian.vondendriesch@credativ.de',
    description='Simple REST API for postgresql on Debian systems.',
    # long_description=readme,
    packages=find_packages(exclude=('tests','doc',)),
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask_RESTful',
        'PyYAML',
    ],
)
