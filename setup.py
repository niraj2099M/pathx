from setuptools import setup

setup(
       name='pathx',
       version='0.1',
       packages=['pathx'],
       install_requires=[
           # List your package dependencies here
       ],
       entry_points={
           'console_scripts': [
               'xpath = pathx.main:main_function',
           ],
       },
)