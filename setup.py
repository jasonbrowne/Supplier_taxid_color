# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in supplier_taxid_color/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('supplier_taxid_color/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='supplier_taxid_color',
	version=version,
	description='Change collor of the text for supplier taxid if the first two digits of a taxid prefix do not match those from the IRS EIN asignment list.',
	author='iXsystems.com',
	author_email='jason@ixsystems.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
