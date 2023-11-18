from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="PBIAT_SELENIUM",
    version=1.0,
    description="Pacote para automatizar rotinas PowerBi",
    long_description=Path('PBIAT_SELENIUM/README.md').read_text(),
    author='Andre Ailton',
    author_email='andre.ailtonf.10@gmail.com',
    keywords=['Selenium','PowerBi','Automatization','automation'],
    packages=find_packages()
)