from setuptools import setup, find_packages


setup(
    name='fandango-aria-plugin',
    version='0.1.4',
    description="A Public Client library and CLI for interacting with ARIA's Data Deposition Service.",
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