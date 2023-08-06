from setuptools import setup, find_packages
import codecs
import os
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

VERSION = '0.0.5'
DESCRIPTION = 'terminal game of Hand Cricket'
# Setting up
setup(
    name='handcric',
    version=VERSION,
    author='Chiranjeev Mishra(chirrumishra)',
    author_email='chirrumishra@gmail.com',
    description=DESCRIPTION,
    packages=find_packages(),
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=['match','python', 'cricket', 'hand cric', 'cricket lib'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
