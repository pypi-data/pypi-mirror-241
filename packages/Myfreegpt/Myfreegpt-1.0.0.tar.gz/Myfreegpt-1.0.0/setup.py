from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='Myfreegpt',
  version='1.0.0',
  author='irfirf123',
  author_email='hack-mr2016@yandex.ru',
  description='This is my first module',
  long_description=readme(),
  long_description_content_type='',
  url='',
  packages=find_packages(),
  install_requires=['requests>=2.25.1',],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='',
  project_urls={},
  python_requires='>=3.7'
)