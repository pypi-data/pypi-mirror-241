from setuptools import setup, find_packages

setup(
    name='octopus_crypto_data',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'time'
    ],
)