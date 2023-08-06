# Copyright (C) 2021 Avery
# 
# This file is part of py18n.
# 
# py18n is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# py18n is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with py18n.  If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup

setup(name='Py18n',
      version='1.0',
      description='I18n for Discord.py',
      author='starsflower',
      url='https://github.com/starsflower/py18n',
      packages=['py18n'],
      package_dir={'py18n': './py18n'},
      install_requires=['discord.py']
     )