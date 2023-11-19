from setuptools import setup, find_packages

setup(
        packages=find_packages(),
        install_requires=[
            'click',
            'pymongo',
            'pypdf',
            'rich',
            'colorama',
            'bibtexparser',
            'habanero',
            'isbnlib',
            'numpy',
            'pytest',
        ],
        entry_points={
            'console_scripts': [
                'bibtheque = bibtheque.cli:bibtheque',
            ]
        }
)
