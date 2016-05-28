# -*- coding: utf-8 -*-

import os
import codecs
import re
from setuptools import setup, find_packages


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-constance-cli',
    version=find_version("constance_cli", "__init__.py"),
    description='Get/Set In-database config settings handled by Django Constance',
    long_description=read('README.rst'),
    author='GrabOne',
    keywords='django constance cli'.split(),
    packages=find_packages(exclude=['constance_cli_test*']),
    install_requires=['django', 'django-constance'],
    platforms='any',
    include_package_data=True,
    license='MIT',
    url='https://bitbucket.org/grabone/django-constance-cli',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent"
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Framework :: Django",
    ],
    zip_safe=False,
)
