from setuptools import setup, find_packages


long_description = """
The numpyk package provides an alternative implementation for mathematical functions, serving as an alternative to NumPy. It is designed for users who seek a lightweight and simplified library for basic mathematical operations in Python. This package is particularly suitable for environments where a reduced memory footprint and faster performance are prioritized.

Key Features:

Lightweight: The package is lightweight, offering a minimalistic set of mathematical functions without the overhead of a full-fledged numerical library.

Simplicity: Aimed at simplicity, numpyk focuses on providing essential mathematical functions commonly used in standard Python environments.

Performance: Tailored for performance in scenarios where the full feature set of NumPy is not required, making it suitable for resource-constrained environments.

Ease of Use: The API is designed to be user-friendly, offering an intuitive interface for performing common mathematical tasks."""

VERSION = '0.0.33'
DESCRIPTION = 'Alternate to numpy'
LONG_DESCRIPTION = 'Alternate to numpy'

# Setting up
setup(
    name="numpyk",
    version=VERSION,
    author="xhi",
    author_email="<changexhiwong@info.in>",
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