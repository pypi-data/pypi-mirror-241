from setuptools import setup, find_packages

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.readlines()
    requirements = [x[:-1] for x in requirements]

setup(
    name='tacrpy',
    version='0.1.18',
    description='Analytická knihovna pro potřeby TA ČR',
    long_description='Knihovna, která slouží pro práci s daty a vypracování analýz TA ČR.',
    author='RozumDoKapsy',
    author_email='david.sulc@tacr.cz',
    # packages=['tacrpy', 'nlp', 'datahub']
    packages=find_packages(),
    project_urls={
        'Documentation': 'https://data.tacr.cz/tacrpy/docs/index.html'
    },
    install_requires=requirements
)
