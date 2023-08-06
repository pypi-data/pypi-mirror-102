# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           setup.py
   Description:
   Author:        
   Create Date:    2020/04/09
-------------------------------------------------
   Modify:
                   2020/04/09:
-------------------------------------------------
"""
from distutils.command.install import INSTALL_SCHEMES
from setuptools import setup, find_packages
from setuptools.command.install import install


for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

setup_args = {
    'cmdclass': {'install': install},
    'name': 'hahaha_utils',
    'author': 'Danny',
    'author_email': 'mrdanny1024@gmail.com',
    'version': "1.0.1",
    'license': 'MIT',
    'description': 'HAHAHA Python3 Utils',
    'long_description': 'HAHAHA Python3 Utils',
    'url': 'https://www.idannywu.com',
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    'classifiers': [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    'package_dir': {
        'hahaha_utils': 'hahaha_utils',
        # 'hahaha_utils.config': 'hahaha_utils/config',
        # 'hahaha_utils.db_utils': 'hahaha_utils/db_utils',
        # 'hahaha_utils.log_handler': 'hahaha_utils/log_handler',
        # 'hahaha_utils.web_request': 'hahaha_utils/web_request'
    },
    'packages': [
        'hahaha_utils',
        # 'hahaha_utils.config',
        # 'hahaha_utils.db_utils',
        # 'hahaha_utils.log_handler',
        # 'hahaha_utils.web_request',
    ],
    # 'packages': find_packages(where="src"),
    'include_package_data': True,
    'install_requires': [
        'pika==1.1.0',
        'pandas==0.25.3',
        'matplotlib==3.2.1',
        'colorama==0.4.3',
        'yagmail==0.11.224',
        'termcolor==1.1.0',
        'camelot_py==0.7.3',
        'requests==2.25.1',
        'kafka_python==2.0.1',
        'pyperclip==1.7.0',
        'lxml==4.5.0',
        'fitz==0.0.1.dev2',
        'baidu_aip==2.2.18.0',
        'scipy==1.4.1',
        'PyMySQL==1.0.2',
        'pyfiglet==0.8.post1',
        'opencv_python==4.2.0.34',
        'numpy==1.19.5',
        'wheel==0.36.2',
        'paramiko==2.7.1',
        'camelot==13.04.13-gpl-pyqt',
        'kafka==1.3.5',
        'mysql_connector_repackaged==0.3.1',
        'Pillow==8.2.0',
        'pip==21.0.1',
        'pycryptodome==3.10.1'
    ],
    'zip_safe': False
}

setup(**setup_args)