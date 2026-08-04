from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    description="ARIA connection for managing access and metadata deposition, primarily through fandanGO",
    long_description=long_description,
    long_description_content_type='text/markdown'
)