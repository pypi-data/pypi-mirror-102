# This is the SETUP file
import setuptools

setuptools.setup(
    name='ProcessEntropy',
    version='0.8.1',
    packages=['ProcessEntropy',],
    license='MIT license',
    author='Tobin South',
    description='A toolkit for calculating process entropy quickly. With specific applications to tweets.',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    url="https://github.com/tobinsouth/ProcessEntropy",
    install_requires=[
        "numba",
        "nltk",
    ],
)