# -*- coding: utf-8 -*-
"""Setup for Drastic-Agent

"""
__copyright__ = "Copyright (C) 2016 University of Maryland"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE, Version 3"


import inspect
import os
from distutils.core import setup
from setuptools import setup, find_packages


setup(
    name='drastic-agent',
    version="1.0",
    description='Drastic agent server',
    extras_require={},
    long_description="Standalone agent for storage management",
    author='Archive Analytics',
    maintainer_email='jansen@umd.edu',
    license="GNU AFFERO GENERAL PUBLIC LICENSE, Version 3",
    url='https://github.com/UMD-DRASTIC/drastic-agent',
    install_requires=[
        "flask==0.10.1",
        "gevent==1.0.2",
        "gunicorn",
        "python-dateutil==2.4.2",
        "nose==1.3.6",
        "crcmod==1.7",
        "blist==1.3.6",
        "paho-mqtt==1.1"
    ],
    entry_points={
        'drivers': [
            'cassandra=drivers.cassandra:Cassandra',
            'disk=drivers.disk:Disk',
        ],
        'console_scripts': [
            # "drastic = drastic.cli:main"
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: System :: Archiving"
    ],
)
