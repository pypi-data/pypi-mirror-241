from distutils.core import setup
from setuptools import find_packages

setup(
  name='FilesNFolders',
  packages=find_packages(),
  version = '0.2',
  license='MIT',
  description = 'Allows the quick generation of files, folders, and their contents.',
  author = 'KayLa Thomas',
  author_email = 'kaylathomas.dev@gmail.com',
  url = 'https://github.com/kaylathomas/FilesNFolders',
  download_url = 'https://github.com/kaylathomas/FilesNFolders/archive/refs/tags/v_0.2.tar.gz',
  keywords = ['files', 'folders', 'generation', 'f-string'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.11'
  ]
)
