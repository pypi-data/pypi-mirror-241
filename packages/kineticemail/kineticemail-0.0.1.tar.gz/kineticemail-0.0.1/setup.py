from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Read/Write PDF Text, Forms, and Metadata.'
LONG_DESCRIPTION = 'A 2023+ package for reading text, metadata, and forms from PDFs with the ability to edit metadata and forms data. Based on prior work by pdfrw and pypdf2 updated for PDF forms changes in latter versions.'

# Setting up
setup(
    name="kineticemail",
    version=VERSION,
    author="Kinetic Seas (Ed Honour / Joe Lehman)",
    author_email="<edward.honour@kineticseas.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['beautifulsoup4'],
    keywords=['python', 'Email Processing'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
