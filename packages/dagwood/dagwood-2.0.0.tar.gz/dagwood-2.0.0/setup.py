from setuptools import setup, find_packages
from dagwood.version import __version__

# Read in the README.md for the long description.
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dagwood',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        # any future dependencies
    ],
    author='Odai Athamneh',
    author_email='heyodai@gmail.com',
    description='Swiss-army knife for Python scripts. Includes logging, HTTP status codes, and more.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/heyodai/dagwood',
)
