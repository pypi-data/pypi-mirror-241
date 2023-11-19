from setuptools import setup, find_packages

setup(
    name='WrapperXSelector',
    version='0.1.0',
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
)