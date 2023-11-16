from setuptools import setup, find_packages
 
classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent"
]
 
setup(
  name='cybercorp',
  version='0.0.1',
  description='.',
  # long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Masimisa',
  author_email='masimisa.elrais@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  # keywords='calculator',
  packages=find_packages(),
  install_requires=[''] 
)