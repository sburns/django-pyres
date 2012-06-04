import os
from setuptools import setup, find_packages
version=__import__('django_pyres').__version__
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name='django-pyres',
    version=version,
    description='django pyres integration',
    long_description=read('README.md'),
    author='Matt George',
    author_email='mgeorge@gmail.com',
    maintainer='Matt George',
    license='MIT',
    url='http://github.com/Pyres/django_pyres',
    packages=find_packages(exclude=['ez_setup', 'example','testapp','tests']),
    include_package_data=True,
    install_requires=[
        'pyres>=1.3',
    ],
    classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python'],
)
