from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='torrearchimedebot',
   version='0.3.1',
   description='A useful bot for Torre Archimede schedule',
   license="GPL3",
   long_description=long_description,
   author='Augugrumi',
   author_email='augugrumi@gmail.com',
   packages=['torrearchimedebot'],  #same as name
   install_requires=['python-telegram-bot'] #external packages as dependencies
)
