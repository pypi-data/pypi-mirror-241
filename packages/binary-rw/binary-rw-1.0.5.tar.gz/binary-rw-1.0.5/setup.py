from distutils.core import setup

VERSION = '1.0.5'
PACKAGE_NAME = 'binary-rw'
AUTHOR = 'Filip K'
AUTHOR_EMAIL = 'fkwilczek@gmail.com'
URL = 'https://gitlab.com/fili_pk/binary-rw'

LICENSE = 'MIT'
DESCRIPTION = 'Simple library for reading binary files.'
LONG_DESCRIPTION = open('README.md', encoding='utf-8').read()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = []

setup(
	name=PACKAGE_NAME,
	version=VERSION,
	author=AUTHOR,
	author_email=AUTHOR_EMAIL,
	description=DESCRIPTION,
	long_description=LONG_DESCRIPTION,
	long_description_content_type=LONG_DESC_TYPE,
	url=URL,
	license=LICENSE,
	install_requires=INSTALL_REQUIRES,
	classifiers=[
		'Programming Language :: Python :: 3',
		'Operating System :: OS Independent',
		'License :: OSI Approved :: MIT License'
	],
	packages=['binary_rw'],
)
