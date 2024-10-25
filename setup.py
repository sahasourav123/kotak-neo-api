from setuptools import setup, find_packages

NAME = "neo-api-client"
VERSION = "1.2.1"
# To install the library, run the following
#
# python setup.py install

with open('requirements.txt') as f:
    REQUIRES = f.read().splitlines()

setup(
    name=NAME,
    version=VERSION,
    description="Neo Trade API",
    author='Sourav Saha',
    author_email='sahasourav123@gmail.com',
    url="",
    keywords=["Neo-Trade API", "Neo Trade API's"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    """
)
