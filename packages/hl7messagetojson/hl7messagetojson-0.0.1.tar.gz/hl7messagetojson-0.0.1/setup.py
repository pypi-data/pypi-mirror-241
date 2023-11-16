# -*- coding: utf-8 -*-

import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="hl7messagetojson",
    version="0.0.1",
    author="Naina Vegunta",
    author_email="naina@dhan.ai",
    description="A simple library to convert HL7 message version 2 to JSON "
                "with human readable description",
    keywords=[
        'HL7', 'Health Level 7', 'healthcare', 'health care', 'medical record'
    ],
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://git-codecommit.us-east-1.amazonaws.com/v1/repos/hl7messagetojson",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={'hl7tojson': ['./data/*/*.json']},
    install_requires=[
        'hl7==0.3.4',
        'six==1.11.0'
    ],
)
