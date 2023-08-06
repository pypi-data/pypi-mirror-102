"""File for build project in python-packet"""

from os.path import join, dirname
from setuptools import setup, find_packages

setup(
    name='splitres',
    version='1.5',
    packages=find_packages(),
    description='Function calculates the min, max, average and sum of '
                'power consumption value and writes this data to a file.',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    url='https://gitwork.ru/barabass/splitres.git',
    author='German Borovkov',
    zip_safe=False,
)
