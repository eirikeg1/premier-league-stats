from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Premier league package for analyzing Premier League statistics'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="premier_league_stats", 
        version=VERSION,
        author="Eirik Eggset",
        author_email="<mail@mail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            'beautifulsoup4',
            'matplotlib',
            'numpy',
            'pandas',
            'pytest',
            'requests',
            'torch',
        ],
        
        keywords=[
            'python',
            'football analytics',
            'machine learning',
        ],
        
        classifiers= [
            "Premier League Analytics Pipeline",
            "Machine Learning Project",
        ]
)