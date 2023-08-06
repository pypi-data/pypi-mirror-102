"""File for build project in python-packet"""

from os.path import join, dirname
from setuptools import setup

setup(
    name='splitres',
    version='1.4',
    packages=['src'],
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    url='https://gitwork.ru/barabass/splitres.git',
    author='German Borovkov'
)
