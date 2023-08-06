import codecs

from setuptools import find_packages, setup

setup(name='gcp_googleanalytics',
    description='A wrapper for the Google Analytics API.',
    long_description=codecs.open('README.rst', 'r', 'utf-8').read(),
    author='Stijn Debrouwere',
    author_email='stijn@debrouwere.org',
    url='https://github.com/konchyts-v/gcp-google-analytics/',
    download_url='https://github.com/konchyts-v/gcp-google-analytics/tarball/master',
    version='1.0.0',
    license='ISC',
    packages=find_packages(),
    keywords='data analytics api wrapper google',
    scripts=[
        'bin/gcp_googleanalytics'
    ],
    include_package_data=True,
    install_requires=[
        'oauth2client<5,>=2.0.1',
        'google-api-python-client==1.12.8',
        'python-dateutil',
        'addressable>=1.4.2',
        'inspect-it>=0.3.2',
        'werkzeug>=0.10',
        'keyring==5.3',
        'click>=6',
        'pyyaml>=3',
        'prettytable>=0.7',
        'colorama>=0.3',
        'snakify>=1.1',
    ],
    test_suite='gcp_googleanalytics.tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        ],
    )
