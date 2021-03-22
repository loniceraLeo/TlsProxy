from setuptools import setup

setup(
    name = 'TLS-Proxy',
    version = '0.2.0',
    packages = ['TLS-Proxy'],
    entry_points = {
        'console_scripts':
            ['tpserver=TLS-Proxy:server']
    }
)