import os
from setuptools import setup

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = os.path.join(lib_folder, 'requirements.txt')
install_requires = []

if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

setup(
    name='stocks_traders_test',
    python_requires=">=3.9",
    version='1.0.0',
    url='',
    author='ksenia',
    author_email='loseva.xenia@gmail.com',
    description='',
    install_requires=['python-dotenv', 'pytest', 'pytest-selenium', 'allure-pytest-bdd', 'pytest-bdd',
                      'allure-python-commons', 'pytest-failed-screenshot']
)