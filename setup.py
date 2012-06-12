import os
import sys

import cactus
import cactus.utils

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup


if "install" in sys.argv:
	
	# Check if we have an old version of cactus installed
	p1 = '/usr/local/bin/cactus.py'
	p2 = '/usr/local/bin/cactus.pyc'
	
	if os.path.exists(p1) or os.path.exists(p2):
		print "Error: you have an old version of Cactus installed, we need to move it:"
		if os.path.exists(p1): print "  sudo rm %s" % p1 
		if os.path.exists(p2): print "  sudo rm %s" % p2
		sys.exit()
	
	# Compress the skeleton files
	os.system('cd cactus/skeleton; find . -name "*.DS_Store" -type f -delete')
	os.system('cd cactus/skeleton; tar -c -f ../../skeleton.tar ./*; gzip ../../skeleton.tar')


setup(
	name='Cactus',
	version='2.0',
	description="Static site generation and deployment.",
	long_description=open('README.markdown').read(),
	url='http://github.com/koenbok/Cactus',
	download_url='http://github.com/koenbok/Cactus',
	author='Koen Bok',
	author_email='koen@madebysofa.com',
	license='BSD',
	packages=['cactus'],
	entry_points={
		'console_scripts': [
			'cactus = cactus.cli:main',
		],
	},
	install_requires=[
		'Django',
		'boto>=2.4.1', 
		'simplejson',
		'baker'
	],
    data_files = ['skeleton.tar.gz'],
	# zip_safe=False,
	tests_require=['nose'],
	test_suite='nose.collector',
	classifiers=[],
)

if "install" in sys.argv:
	os.system('rm skeleton.tar.gz')