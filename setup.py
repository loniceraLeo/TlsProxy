from setuptools import setup

setup(
    name = 'TlsProxy',
    version = '0.2.0',
    descriptor = 'a safe http proxy over tls',
    long_description = 'README.md',
    author = 'github.com/loniceraLeo',
    url = 'https://www.github.com/loniceraLeo/TlsProxy',
    packages = ['TlsProxy'],
    python_requires = '>=3.6.0',
    license = 'GPL',
    entry_points = {
        'console_scripts':
            [
                'tpserver = TlsProxy.server:entry',
                'tpclient = TlsProxy.client:entry'
            ]
    }
)