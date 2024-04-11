from setuptools import setup, find_packages


setup(
    name='fandango-aria-plugin',
    version='0.0.4',
    description="A Public Client library and CLI for interacting with ARIA's Data Deposition Service.",
    author="Lui Holliday, Instruct-ERIC",
    author_email="lui.holliday@instruct-eric.org",
    license='MIT',
    packages=find_packages(),
    url='https://github.com/FragmentScreen/fandango-aria-plugin',
    install_requires=[
        'click',
        'requests',
        'python-dotenv',
        'keyring',
        'questionary',
        'inquirer',
        'datetime',
        'PyYAML'
    ],
    entry_points={
        'console_scripts': [
            'fandango=fandango.commands.cli:cli',
        ],
    },
)