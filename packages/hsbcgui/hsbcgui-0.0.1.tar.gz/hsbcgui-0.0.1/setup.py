from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
def app():
  with open('example.txt', 'a') as file:
    # Append content to the file
    file.write('\nThis line is appended.')


class PostInstallCommand(install):
    def run(self):
      app()
        

setup(
  name='hsbcgui',
  version='0.0.1',
  description='Improving my Python project',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Joshua Lowe',
  author_email='josh@edublocks.org',
  license='MIT', 
  classifiers=classifiers,
  keywords='calc', 
  packages=find_packages(),
  install_requires=[''] 
)
