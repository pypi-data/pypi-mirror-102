# This file is placed in the Public Domain.

from setuptools import setup

def read():
    return open("README.rst", "r").read()

setup(
    name='genocide',
    version='31',
    url='https://github.com/bthate/genocide',
    author='Bart Thate',
    author_email='bthate@dds.nl', 
    description="The king of the netherlands commits genocide - http://genocide.rtfd.io #ggz #gifpil",
    long_description=read(),
    license='Public Domain',
    packages=["gcd", "genocide"],
    namespace_packages=["gcd", "genocide"],
    zip_safe=False,
    scripts=["bin/gcd", "bin/genocide", "bin/genocidectl"],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
 