from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'Simple library to get information about pokemon'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

# Setting up
setup(
    name="PokePoke",
    version=VERSION,
    author="SeladaKeju",
    author_email="<rizqiadit2430@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/SeladaKeju/Pokemon',
    packages=find_packages(),
    install_requires=[],
    keywords=['Poke', 'Pokemon'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)