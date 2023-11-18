from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'Negara Informasi Inform Negara negara '

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

# Setting up
setup(
    name="joatcountry7",
    version=VERSION,
    author="scaem007",
    author_email="<syahrulromadhonmuhamamd@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/syahrulcaem/joatcountry7',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    keywords=['country','negara'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)