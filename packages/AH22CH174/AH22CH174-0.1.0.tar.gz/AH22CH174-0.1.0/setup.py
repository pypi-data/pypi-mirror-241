from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='AH22CH174',
  version='0.1.0',
  description='A very basic calculator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Tanishq JM',
  author_email='tanishqurmi@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='result', 
  packages=find_packages(),
  install_requires=['pandas','openpyxl'] 
)