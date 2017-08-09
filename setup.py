#!/usr/bin/env python

from setuptools import setup, find_packages
from send2kindle import _version

setup(
    name='send2kindle',
    version=_version,
    packages=find_packages(exclude=('tests', 'tests.*')),
    entry_points={
        'console_scripts': ['send2kindle = send2kindle.__main__:main'],
    },
    author='wixb50',
    author_email='wixb50@gmail.com',
    description='CLI tool for sending files via email to your Kindle device',
    long_description='Configure your email and then send any files provided as program arguments as email attachments to your Kindle device.',
    keywords='commandline Kindle email',
    license='GNU Affero GPL v3+',
    url='https://github.com/wixb50/send2kindle',
    download_url='https://github.com/wixb50/send2kindle',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Email',
        'Topic :: Utilities',
    ]
)
