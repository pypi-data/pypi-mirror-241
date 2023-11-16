from setuptools import setup, find_packages


long_description = "Alternate"

VERSION = '0.0.32'
DESCRIPTION = 'Alternate to numpy'
LONG_DESCRIPTION = 'Alternate to numpy'

# Setting up
setup(
    name="numpyk",
    version=VERSION,
    author="someone",
    author_email="<someone@info.in>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)