from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pysmart-ai',
  version='0.0.4',
  description='A smarter way of automating machine learning and deep learning 🔥',
  long_description=open('Readme.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Abdul Azim',
  author_email='abdulazim0402@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='AutoML', 
  packages=find_packages(),
  install_requires=['pycaret'] ,
)