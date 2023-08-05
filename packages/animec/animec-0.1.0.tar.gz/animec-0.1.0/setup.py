from setuptools import setup, find_packages

version = '0.1.0'

with open('requirements.txt', 'r') as f:
  requirements = f.read().split('\n')

with open('README.md', 'r', encoding = 'utf-8') as f:
  long_description = f.read()

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  "Topic :: Education :: Testing",
  "Topic :: Software Development :: Libraries"
]
 
setup(
  name = 'animec',
  version = version,
  description = 'An unofficial API to get data about anime characters, anime news, anime info and more.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/DriftAsimov/animec',  
  author = 'DriftAsimov',
  author_email = 'driftasimov@gmail.com',
  license = 'MIT', 
  classifiers = classifiers,
  keywords = ['animecharacter anime api character myanimelist news animenews animeinfo'], 
  packages = find_packages(),
  install_requires = requirements 
)