from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='felegToo',
  version='0.0.2',
  author='feleg',
  author_email='false.fas527@gmail.com',
  description='cftools',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://cubefel.netlify.app',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  keywords='cfPass',
  python_requires='>=3.6'
)