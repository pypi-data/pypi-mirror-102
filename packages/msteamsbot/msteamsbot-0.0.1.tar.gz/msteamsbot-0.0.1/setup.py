from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='msteamsbot',
  version='0.0.1',
  description='msteamsbot is a package that allows you do stuff with  Ms-Teams. ',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Parteek Deol',
  author_email='610078787@musd.net',
  license='MIT', 
  classifiers=classifiers,
  keywords='robot', 
  packages=find_packages(),
  install_requires=[''] 
)
