# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '1.1'

setup(
    name='matem.congresos',
    version=version,
    description="Congres type for the Institute of Mathematics",
    long_description=open('README.rst').read() + '\n' +
    open('docs/CHANGES.txt').read(),
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Plone',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    platforms='Any',
    author='Informática Académica',
    author_email='informatica.academica@im.unam.mx',
    url='https://github.com/imatem/matem.congresos',
    license='GPL',
    namespace_packages=['matem'],
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    extras_require={
        'develop': [
        ],
        'test': [
            'plone.app.testing',
        ],
    },
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
