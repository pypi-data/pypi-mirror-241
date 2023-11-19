from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
name = 'ORELWEbyST',
long_description    = long_description,
long_description_content_type='text/markdown',
version = '0.3',
author = 'Jaehwan Park',
author_email = 'jpark127@utk.edu',
python_requires = '>=3.6'
)
