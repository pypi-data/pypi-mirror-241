from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'Negara Informasi Inform Negara'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

# Setting up
setup(
    name="modulsurahdann",
    version=VERSION,
    author="ardan",
    author_email="<ardanferdiansah03@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/dannfrd/modulsurahdann',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    keywords=['surah', 'search'],
    classifiers=[
        'Development Status :: 1 - Planning',
        ],
)