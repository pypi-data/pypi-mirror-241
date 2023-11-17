#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup
from owega.changelog import OwegaChangelog as oc

desc = open('README.md').read()
desc += '\n\n'
desc += "## CHANGELOG: "
desc += '\n```\n'
desc += oc.log
desc += '\n```\n'

setup(
	name='owega',
	version='4.5.2',
	packages=[
		'owega',
		'owega.changelog',
		'owega.config',
		'owega.OwegaFun',
		'owega.conversation',
	],
	install_requires=[
		'openai>=1.1.1',
		'prompt_toolkit>=3.0',
		'requests>=2.0',
		'beautifulsoup4>=4.0',
		'lxml>=4.0',
		'tiktoken>=0.5.1',
		'json-five>=1.1.0',
	],
	scripts=[
		'scripts/owega',
	],
	long_description=desc,
	long_description_content_type='text/markdown',
	project_urls={
		'Source': 'https://git.pyrokinesis.fr/darkgeem/owega',
	},
)
