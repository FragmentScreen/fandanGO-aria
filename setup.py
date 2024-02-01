from setuptools import setup, find_packages

setup(
    name='aria-data-deposition',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'aria-login=cli.cli:login',
            'aria-help=cli.cli:help'
        ],
    },
)