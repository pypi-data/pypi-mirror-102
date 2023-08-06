# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:39:35 2021

@author: NSi
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Environment :: Win32 (MS Windows)',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Intended Audience :: End Users/Desktop',
    'License :: Free For Educational Use',
    'Programming Language :: Python :: 3.7',
    'Natural Language :: English'
  ]

setup(
  name='gencon',
  version='1.1.1',
  author="Nallathamby Sivasithamparam",
  author_email='nallathamby.siva@ngi.no',  
  description="GENCON program is used to calculate C1, C2, C3 for model coefficents  \
               for general clay model in INFIDEL/INFIDEP",
  Long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  license="NGI license",
  include_package_data=True,
  classifiers=classifiers,
  zip_safe=False,
  install_requires=[''],
  keywords='general clay model'
)
