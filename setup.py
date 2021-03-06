# -*- encoding: utf-8 -*-
from distutils.core import setup

setup(
    name='datetime_trunc',
    version='1.0.0',
    url='https://github.com/pb-/datetime_trunc',
    author='Björn Andersson / Media Pop',
    author_email='bjorn@mediapop.co',
    description='Truncate datetime objects to a set level of precision',
    license='BSD',
    long_description=open('README.rst').read(),
    packages=['datetime_trunc'],
    package_data={
        '': ['README.rst']
    },
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose>=1.2.1'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
)
