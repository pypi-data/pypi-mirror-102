from setuptools import setup, find_packages
import codecs
import os
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


VERSION = '0.0.5'
DESCRIPTION = 'It Displays Cricket Score'

# Setting up
setup(
    name='iplscore',
    version=VERSION,
    author='Chiranjeev Mishra(chirrumishra)',
    author_email='chirrumishra@gmail.com',
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
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

