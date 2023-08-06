from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='hello_wor',
  version='0.0.1',
  description='A very simple library',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Abdul Azim',
  author_email='abdulazim0402@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='hello world', 
  packages=find_packages(),
  install_requires=[''] 
)