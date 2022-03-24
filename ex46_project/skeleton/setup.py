try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': 'My email',
    'version': '0.1',
    'install_requires': ['none'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

# 解包字典 config, 将 key 和 value 传给 setup
setup(**config)
