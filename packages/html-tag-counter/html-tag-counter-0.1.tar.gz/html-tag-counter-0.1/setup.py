from setuptools import setup, find_packages

setup(
    name="html-tag-counter",
    packages=find_packages(),   
    install_requires=[
        "beautifulsoup4 == 4.9.3",
        "bs4 == 0.0.1",
        "PyYAML == 5.4.1",
        "SQLAlchemy == 1.4.15",
        "tld == 0.12.5",
        ],
    version="0.1",
    author="Htosci Dziesci",
    author_email="htosci_dziesci@gmail.com",
    description="Count Tags",
    license="MIT",
)
