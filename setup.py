
from distutils.core import setup

setup(
    name='baymax',
    version='0.0.4',
    author='Vijay Sharma Yellepeddi',
    author_email='vijay.tyren@gmail.com',
    packages=['baymax','baymax.core', 'baymax.test','baymax.examples'],
    url='http://pypi.python.org/pypi/baymax/',
    license='LICENSE.txt',
    description='Data Visualization Template Engine for Django/Flask',
    long_description=open('README.txt').read(),
)
