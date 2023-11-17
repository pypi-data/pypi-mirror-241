from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'Simple library bikin pusing'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

# Setting up
setup(
    name="informasi_mahasiswa",
    version=VERSION,
    author="rafiiqbal2407",
    author_email="<rafiiqbal2407@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/iqbull2244/iball',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    keywords=['mahasiswa'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)