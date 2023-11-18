from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='cloudboot',
    version='0.1.0-beta2',
    description='A groovy collection of easy-peasy scripts and serverless ready templates for Google Cloud serverless computing!',
    url='https://cloudboot.github.io',
    author='Lahiru Pathirage',
    author_email='lpsandaruwan@gmail.com',
    license='MIT',
    scripts=['./bin/cloudboot'],
    packages=find_packages(),
    install_requires=['click', 'inquirerpy', 'requests', 'termcolor', 'pyfiglet'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
