from setuptools import setup
from setuptools import find_packages

setup(name='cython-manager',
      version='0.0.1',
      author='Alexey Makridenko',
      author_email='makridenko.a@yandex.ru',
      scripts=['CythonManager/bin/cython-manager.py'],
      entry_points={'console_scripts': [
            'cython-manager = CythonManager.core.managment:execute_from_command_line'
      ]},
      packages=find_packages())
