from setuptools import setup, find_packages


setup(
    name='fandango',
    version='0.0.2',
    description="A Public Client library and CLI for interacting with ARIA's Data Deposition Service.",
    author="Lui Holliday, Instruct-ERIC",
    author_email="lui.holliday@instruct-eric.org",
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'python-dotenv',
        'keyring'
    ],
    entry_points={
        'console_scripts': [
            'fandango=cli:cli',
        ],
    },
)