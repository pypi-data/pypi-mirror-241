from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='StringFuncs',
    version='0.0.3.5',
    author='Samuel Morris',
    author_email='samuelmorris333221@gmail.com',
    description='A package for string manipulation, has ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SamuelMorrisProjects/StringFuncs',
    license='MIT',
    license_files = ('LICENSE.txt',),
    packages=['StringFuncs'],
    install_requires=[
    ]
)