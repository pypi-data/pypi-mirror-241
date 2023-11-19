from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
    
setup(
    name='WrapperXSelector',
    version='0.1.1',
    author='Kallol Naha',
    author_email='kallolnaha@gmail.com',
    description='WrapperXSelector is an intuitive tool that empowers users to effortlessly create scraping wrappers. Seamlessly combining the art of crafting with powerful scraping capabilities, it allows users to select and store XPath configurations for later use in efficient website data harvesting.',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    long_description=long_description,
    long_description_content_type='text/markdown'
)