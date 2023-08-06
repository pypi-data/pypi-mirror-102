#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2017 Canonical Ltd.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

import pkg_resources
import setuptools
VERSION = '0.0'
setuptools.setup(
        name='qihoo_for_t',
        version=VERSION,
        description='test',
        author='lee',
        author_email='test@qq.com',
        license='LGPLv3',
        packages=setuptools.find_packages(),
        install_requires=['numpy']
        #install_requires=parse_requirements_file('requirements.txt'),
        #test_suite='acceptable.test_acceptable',
        #tests_require=parse_requirements_file('requirements-dev.txt'),
        #python_requires = 'test'
    )


