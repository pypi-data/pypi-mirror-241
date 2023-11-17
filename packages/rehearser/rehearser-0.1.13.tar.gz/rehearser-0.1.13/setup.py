import boto3
from setuptools import find_packages, setup

setup(
    name="rehearser",
    version="0.1.13",
    url="https://github.com/kevinchwong/rehearser-examples",
    author="Kevin C. Wong",
    author_email="kevinchwong@gmail.com",
    description="Rehearser makes writing reliable unit tests super easy!",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=["boto3"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='unit testing, contract testing, testing tools, open source, developer tools, rehearsal, proxy, rehearser',

)