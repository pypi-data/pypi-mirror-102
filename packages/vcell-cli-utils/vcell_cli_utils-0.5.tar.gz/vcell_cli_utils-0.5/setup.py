
from os import path
from distutils.core import setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
  name = 'vcell_cli_utils',
  packages = ['cli_util'],
  version = '0.5',
  license='MIT',
  description = 'Python utility package for VCell CLI Java App',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Virtual Cell',
  author_email = 'marupilla@uchc.edu',
  url = 'https://github.com/virtualcell/vcell_cli_utils',
  download_url = 'https://github.com/virtualcell/vcell_cli_utils/archive/refs/tags/0.1.tar.gz',
  keywords = ['HDF5', 'Visualization', 'YAML', 'Fire'],
  install_requires=[
      'biosimulators_utils', 
      'fire', 
      'pyyaml', 
      'pandas', 
      'matplotlib', 
      'seaborn', 
      'python-libsedml',
      'python-libsbml'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)