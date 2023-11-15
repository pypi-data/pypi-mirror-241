from setuptools import setup, find_packages

setup(
    name='embeocr',
    version='0.2',
    author='trangvv2',
    author_email='vantrangeuro@gmail.com',
    description='Description of my package',
    packages=find_packages(),    
    install_requires=['transformers', 
                      'torch==2.0.1', 
                      'numpy'],
)