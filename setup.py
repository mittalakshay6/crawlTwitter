#!/usr/bin/env python3

from setuptools import setup, find_packages


with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

setup(
    name='crawlTwitter',
    version='1.0.0',
    description='Tool to crawl twitter for specific keywords and thereafter store the results in json file or MongoDB',
    author=['Akshay Mittal'],
    author_email='it158040@mnnit.ac.in',
    license='Pyenoma',
    packages=find_packages(exclude=["build.*", "tests", "tests.*"]),
    install_requires=required,
    entry_points={
        "console_scripts": [
            "crawlTwitter = crawlTwitter.main:main"
        ]
    })
