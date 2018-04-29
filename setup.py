import os
from setuptools import setup, find_packages


setup(
    name='django_hashids',
    version=0.0,
    author='Code Hat Labs, LLC',
    author_email='dev@codehatlabs.com',
    url='https://github.com/CodeHatLabs/django_cognito',
    description='Django tools for obfuscating url arguments with hashids',
    packages=find_packages(),
    long_description="",
    keywords='python django hashids',
    zip_safe=False,
    install_requires=[
        'hashids'
    ],
    test_suite='',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
