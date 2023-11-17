from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'A simple Python library for basic mathematical calculations'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

# Setting up
setup(
    name="mymathlib",
    version=VERSION,
    author="AIvanCP",
    author_email="<angvacp@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/AIvanCP',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    keywords=[],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)