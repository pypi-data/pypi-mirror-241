from setuptools import setup, find_packages

setup(
    name="PBI_SELENIUM",
    version=1.0,
    description="package for routine operations in power bi",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    author='Andre Ailton',
    author_email='andre.ailtonf.10@gmail.com',
    keywords=['Selenium','PowerBi','Automatization','automation'],
    packages=find_packages()
)