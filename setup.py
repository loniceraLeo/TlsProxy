from setuptools import setup

setup(
    name = 'TlsProxy',
    version = '0.2.0',
    author = 'github.com/loniceraLeo',
    packages = ['TlsProxy'],
    entry_points = {
        'console_scripts':
            [
                'tpserver = TlsProxy.server:entry',
                'tpclient = TlsProxy.client:entry'
            ]
    }
)