__author__ = 'Alex Rogozhnikov'

from setuptools import setup

setup(
    name="newpyter",
    version='0.3.0',
    packages=['newpyter', 'newpyter.storage'],

    install_requires=[
        # useful for grammars
        'parsimonious',
        'nbformat',
        'sh',
        # download / upload to aws
        'boto3',
        # to parse configuration
        'toml',
        # for exception, but is should be installed by jupyter
        'tornado',
    ],
)