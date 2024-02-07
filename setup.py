from setuptools import setup, find_packages

setup(
    name='aria-data-deposition',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'aria=cli.cli:help',
            'aria-login=cli.cli:login',
            'aria-help=cli.cli:help',
            'aria-get=cli.cli:set_token_password'
        ],
    },
)