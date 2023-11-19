from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.8'
DESCRIPTION = 'ganeshmath'
LONG_DESCRIPTION = 'A package to perform arithmetic operations easily'

# Setting up
setup(
    name="ganeshmath",
    version=VERSION,
    author="Ganesh Kavhar",
    author_email="ganeshkavhar8@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['arithmetic', 'math', 'mathematics', 'python', 'ganeshkavhar' ,'ganeshkavhar sql'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)