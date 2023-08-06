from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  # Change OS if you are on Mac or Linux
  'License :: OSI Approved :: MIT License',
  # Change the license above if you want.
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Helloworld20211234',
  # Change name to your package name.
  version='0.0.1',
  description='says hello world. Learn how to make your own Python package by visiting my blog, https://ryan-chou.medium.com/',
  # Put a short description here.
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  # We'll create README.txt and CHANGELOG.txt later
  url='', 
  # place where code is hosted, optional.
  author='Ryan Chou',
  # add author here
  author_email='',
  # you can add this if you want
  license='MIT', 
  # change this license if you want
  classifiers=classifiers,
  keywords='KEYS', 
  # add any keywords you want.
  packages=find_packages(),
  install_requires=[''] 
  # add any dependencies for this package such as numpy or tensorflow
)