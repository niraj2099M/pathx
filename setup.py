from setuptools import setup

setup(
       name='pathx',
       version='0.2',
       packages=['pathx'],
       install_requires=[
           # List your package dependencies here
       ],
       entry_points={
           'console_scripts': [
               'pathx = pathx.main:main_function',
           ],
       },
)
