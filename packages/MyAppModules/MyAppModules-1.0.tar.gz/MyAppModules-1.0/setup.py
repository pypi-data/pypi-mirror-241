
from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='MyAppModules',
    version='1.0',
    packages=['myapp'],
    install_requires=requirements,
    author='Farah Ben Mohamed',
    author_email='farahbenmohamed.carnelian@gmail.com',
    description='MyAppModules',
)
#username : farahCarnelian / password : Py2023_test*