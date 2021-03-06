from setuptools import setup, find_packages

requires=['rauth', 'six']

setup(name='contextio',
    version='v1.10.2',
    description='Library for accessing the Context.IO API v2.0 in Python',
    author='Tony Blank, Jesse Dhillon',
    author_email='tony@context.io, jesse@deva0.net',
    url='http://context.io',
    keywords=['contextIO', 'imap', 'oauth'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    download_url='https://github.com/contextio/Python-ContextIO/archive/v1.10.2.tar.gz',
)
