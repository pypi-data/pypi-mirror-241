from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'A Python package for interacting with the City4u API'
LONG_DESCRIPTION = 'This package provides a simple and intuitive interface for interacting with the City4u API. It includes features for getting water consumption data and customer info.'

setup(
    name="city4uAPI",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Alon Teplitsky",
    author_email="alon.ttp@gmail.com",
    license='MIT',
    url="https://github.com/0xAlon/city4uAPI",
    packages=find_packages(),
    install_requires=["requests", "urllib3"],
    keywords='city4uAPI'
)
