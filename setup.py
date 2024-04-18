from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='fandango-aria-plugin',
    version='0.2.0',
    description="A Public Client library and CLI for interacting with ARIA's Data Deposition Service.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Lui Holliday, Instruct-ERIC",
    author_email="lui.holliday@instruct-eric.org",
    license='MIT',
    package_data={'fandango': ['config/*.yml']},
    packages=find_packages(exclude=['ez_setup', 'examples','tests', 'tests.*', 'release']),
    include_package_data=True,
    url='https://github.com/FragmentScreen/fandango-aria-plugin',
    install_requires=[
        'click',
        'requests',
        'keyring',
        'questionary',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'fandango=fandango.commands.cli:cli',
        ],
    },
)