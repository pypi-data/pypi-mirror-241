from time import time
from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='abstract_utilities',
    version='0.2.2.28',
    author='putkoff',
    author_email='partners@abstractendeavors.com',
    description='abstract_utilities is a collection of utility modules providing a variety of functions to aid in tasks such as data comparison, list manipulation, JSON handling, string manipulation, mathematical computations, and time operations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AbstractEndeavors/abstract_utilities',
    classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.11'],
    install_requires=['yt_dlp>=2023.10.13', 'tiktoken>=0.5.1', 'pexpect>=4.8.0', 'abstract_security>=0.0.1', 'pathlib>=1.0.1'],
    package_dir={'': 'src'},
    packages=find_packages(),
    requires_python='>=3.8',
)