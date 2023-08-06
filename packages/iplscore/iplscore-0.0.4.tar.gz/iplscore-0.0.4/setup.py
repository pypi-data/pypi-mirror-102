from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.4'
DESCRIPTION = 'It Displays Cricket Score'

# Setting up
setup(
    name='iplscore',
    version=VERSION,
    author='Chiranjeev Mishra(chirrumishra)',
    author_email='chirrumishra@gmail.com',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['bs4','requests'],
    keywords=['python', 'cricket', 'ipl', 'iplscore'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

