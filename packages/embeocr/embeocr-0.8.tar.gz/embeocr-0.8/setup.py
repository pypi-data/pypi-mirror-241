from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='embeocr',
    version='0.8',
    author='trangvv2',
    python_requires='<=3.11.6',
    author_email='vantrangeuro@gmail.com',
    description='Description of my package',
    readme = "README.md",
    packages=find_packages(),    
    install_requires=['transformers', 
                      'torch==2.0.1', 
                      'numpy'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)