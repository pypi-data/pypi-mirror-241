from setuptools import setup, find_packages
from os import path
# twine upload dist/*
# python setup.py bdist_wheel
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.6',
  'Programming Language :: Python :: 3.7',
  'Programming Language :: Python :: 3.8',
  'Programming Language :: Python :: 3.9',
]
 
setup(
  name='vis-lab',
  version='1.0.3',
  description='a system reinforcement learning game splendor for vis intern',
  # long_description=open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8').read(),
  url='',  
  author='Ngo Xuan Phong',
  author_email='phong@cht.edu.vn',
  license='MIT', 
  classifiers=classifiers,
  keywords='python',
  packages=find_packages(),
  install_requires=[
    'numpy == 1.21.6',
    'numba == 0.56.3',
    ],
  python_requires='>=3.6',
  include_package_data=True
)