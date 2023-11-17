from setuptools import setup, find_packages
from os import path

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

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
  version='1.0.5',
  description='a system reinforcement learning library',
  url='',  
  author='Ngo Xuan Phong',
  author_email='phong@cht.edu.vn',
  license='MIT', 
  classifiers=classifiers,
  keywords='python',
  package_dir = {"": "src"},
  packages=find_packages(where="src"),
  install_requires=[
    'numpy == 1.21.6',
    'numba == 0.56.3',
    ],
  python_requires='>=3.6',
  include_package_data=True
)