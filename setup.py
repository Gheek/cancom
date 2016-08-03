from distutils.core import setup

setup(
    name='cancom',
    version='0.1.0',
    author='Kevin Lamshoeft',
    author_email='post@lamshoft.de',
    packages=['cancom', 'cancom.test', 'cancom.hw', 'cancom.utils', 'cancom.proto'],
    scripts=[],
    url='https://github.com/Gheek/cancom',
    license='GPLv3',
    description='Library for interacting with Controller Area Network (CAN)',
    long_description=open('README.rst').read(),
    classifiers=['Development Status :: 3 - Alpha',
		 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		 'Topic :: Software Development :: Libraries',
		 'Topic :: Software Development :: Embedded Systems']


)
