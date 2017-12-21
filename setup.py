# This file is part of TorreArchimedeBot.
#
# TorreArchimedeBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TorreArchimedeBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TorreArchimedeBot.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='torrearchimedebot',
   version='0.3.3',
   description='A useful bot for Torre Archimede schedule',
   license="GPL3",
   long_description=long_description,
   author='Augugrumi',
   author_email='augugrumi@gmail.com',
   packages=['torrearchimedebot'],  #same as name
   install_requires=['python-telegram-bot'] #external packages as dependencies
)
