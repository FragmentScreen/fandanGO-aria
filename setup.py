from setuptools import setup, find_packages

setup(
    name='aria-data-deposition',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'python-dotenv',
        'keyring'
    ],
    entry_points={
        'console_scripts': [
            'aria=cli.cli:help',
            'aria-login=cli.cli:login',
            'aria-help=cli.cli:help',
            'aria-get=cli.cli:get_token_password',
            'aria-bucket-create=cli.cli:create_bucket',
            'aria-bucket-list=cli.cli:list_buckets',
            'aria-record-create=cli.cli:create_record',
            'aria-record-list=cli.cli:list_records',
            'aria-field-create=cli.cli:create_field',
            'aria-field-list=cli.cli:list_fields'
        ],
    },
)