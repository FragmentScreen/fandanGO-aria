from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='fandanGO-aria',
    version='2.2.4',
    description="ARIA connection for managing access and metadata deposition, primarily through fandanGO",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Lui Holliday, Instruct-ERIC",
    author_email="lui.holliday@instruct-eric.org",
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples','tests', 'tests.*', 'release']),
    url='https://github.com/FragmentScreen/fandanGO-aria',
    install_requires=[
        'click',
        'requests',
        'keyring',
        'python-dotenv',
        'questionary',
        'PyYAML',
        'cryptography',
    ],
    entry_points={
        'console_scripts': [
            'goaria=fGOaria.commands.cli:cli',
        ],
    }
)