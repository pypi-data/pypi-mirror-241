from setuptools import setup

setup(
    name ='inpinitiFinance',
    version = '1.0.1',
    description = 'finance data',
    author = 'inpiniti',
    author_email = 'younginpiniti@gmail.com',
    url='https://github.com/inpiniti/inpinitiFinance',
    install_requires=['OpenDartReader', 'pandas', 'requests',],
    py_modules = ['ifinance'],
    keywords = ['finance', 'stock', 'data', 'inpiniti', 'dart', 'krx'],
)