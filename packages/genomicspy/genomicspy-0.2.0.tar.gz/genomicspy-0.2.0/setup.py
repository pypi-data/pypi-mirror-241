#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

version = '0.2.0'

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

#with open('requirements.txt') as requirements_file:
#    requirements = [line.strip() for line in requirements_file]
#test_requirements = [ ]

setup(
    author="Vivian Leung",
    author_email='leung.vivian.w@gmail.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License version 2.1',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    description="Tools for manipulating vcfs doing genomics work",
    entry_points={
        'console_scripts': [
            # 'genomicspy=genomicspy.cli:main',
            'alleles2fasta=genomicspy.alleles2fasta:main',
        ],
    },
 #   install_requires=requirements,
    license="LGPL-2.1",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords=['genomicspy', 'vcf', 'genomics'],
    name='genomicspy',
    packages=find_packages(include=['genomicspy', 'genomicspy.*']),
    test_suite='tests',
#    tests_require=test_requirements,
    url='https://github.com/vivianleung/genomicspy',
    version=version,
    zip_safe=False,
)
