from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'Library Python untuk menghitung keliling balok.'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

# Setting up
setup(
    name="hitungbalok_30",
    version=VERSION,
    author="rizalfarhan",
    author_email="<rizalfarhannanda@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/rizalfarhan/Hitung-Balok',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    keywords=['balok','ruang'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)