from setuptools import find_packages, setup
from pip._vendor import tomli

# For consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

with open('pyproject.toml', 'r') as f:
    VERSION = tomli.load(f)['tool']['commitizen']['version']

DESCRIPTION = 'A python library for authenticating requests for various google services including ``gmail``, ``youtube``, ``drive`` and ``calendar``.'

key_words = [
    'google-auth',
]

install_requires = [
    'google-api-python-client',
    'google-auth-oauthlib',
    'pydantic',
    'pydantic-settings'
]

setup(
    name='oryks-google-oauth',
    packages=find_packages(
        include=[
            'oryks_google_oauth',
        ]
    ),
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,
    url='https://youtube-wrapper.readthedocs.io/en/latest/index.html',
    author='Lyle Okoth',
    author_email='lyceokoth@gmail.com',
    license='MIT',
    install_requires=install_requires,
    keywords=key_words,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent'
    ],
)
