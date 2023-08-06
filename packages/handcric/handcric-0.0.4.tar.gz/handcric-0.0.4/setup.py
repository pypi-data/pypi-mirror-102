from setuptools import setup, find_packages
import codecs
import os

# here = os.path.abspath(os.path.dirname(__file__))

# with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()


VERSION = '0.0.4'
DESCRIPTION = 'terminal game of Hand Cricket'
# Setting up
setup(
    name='handcric',
    version=VERSION,
    author='Chiranjeev Mishra(chirrumishra)',
    author_email='chirrumishra@gmail.com',
    description=DESCRIPTION,
    packages=find_packages(),
    #long_description=long_description,

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
