#!/usr/bin/env python3
import setuptools
import pathlib


setuptools.setup(

	name='lexio',
	version='0.0.3',
	description='lexIO is a Natural Language Processing (NLP) library in python that is built on top of the numpy library.',
	long_description=pathlib.Path('readme.md').read_text(),
	long_description_content_type = 'text/markdown',
	author='Rijul Dhungana',
	author_email = 'rijuldhungana37@gmail.com',
	classifiers=
	[
		"Development Status :: 3 - Alpha" ,
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 3",
		"Topic :: Utilities"
	],
	python_requires = ">=3.7",
	install_requires=['numpy'],
	packages=setuptools.find_packages(),
	include_packages=True,
	keywords = ['lexio', 'nlp', 'language']
	)
