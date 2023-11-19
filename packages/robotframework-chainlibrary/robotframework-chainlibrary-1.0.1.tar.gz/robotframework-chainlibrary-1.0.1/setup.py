from setuptools import setup

VERSION = '1.0.1'

with open('README.md') as readme:
    description = readme.read()

setup(
    name='robotframework-chainlibrary',
    package_dir={'': 'src'},
    packages=['ChainLibrary'],
    version=VERSION,
    description='Robot Framework library for running keywords in chain',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/crsdet/robotframework-chainlibrary',
    author='Mauricio Gutierrez',
    author_email='103621275+crsdet@users.noreply.github.com',
    license='GPL-3.0',
    keywords='robotframework',
    install_requires=['robotframework'],
    platforms='any',
)
