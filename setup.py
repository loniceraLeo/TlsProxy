from setuptools import setup

with open('./README.md', 'r', encoding='utf-8') as f:
    ld = f.read()

setup(
    name = 'TlsProxys',
    version = '1.0.5',
    description = 'a safe http proxy over tls',
    long_description_content_type = 'text/markdown',
    long_description = ld,
    author = 'github.com/loniceraLeo',
    url = 'https://www.github.com/loniceraLeo/TlsProxy',
    packages = ['TlsProxy'],
    platforms = ['windows', 'linux'],
    python_requires = '>=3.7.0',
    license = 'GPL',
    entry_points = {
        'console_scripts':
            [
                'tpserver = TlsProxy.server:entry',
                'tpclient = TlsProxy.client:entry'
            ]
    }
)