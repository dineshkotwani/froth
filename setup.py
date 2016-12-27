
from distutils.core import setup

setup(
    name='froth',
    version='0.0.1',
    author='Vijay Sharma Yellepeddi',
    author_email='vijaysharma.yellepeddi@gmail.com',
    packages=['froth','froth.core', 'froth.test','froth.examples'],
    url='http://pypi.python.org/pypi/froth/',
    license='LICENSE.txt',
    description='Data Visualization Template Engine for Django/Flask=',
    long_description=open('README.txt').read(),
)
