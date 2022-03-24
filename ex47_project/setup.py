try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'CYLK',
    'url': 'https://...',
    'download_url': 'https://...',
    'author_email': 'CYLK_Cylkun@163.com',
    'version': '0.1',
    'install_requires': ['Windows 10'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
