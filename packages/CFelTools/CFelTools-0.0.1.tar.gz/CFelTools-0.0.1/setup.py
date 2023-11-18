from setuptools import setup, find_packages


def readme():
  with open('readme.md', 'r') as f:
    return f.read()


setup(
  name='CFelTools',
  version='0.0.1',
  author='feleg',
  author_email='false.fas527@gmail.com',
  description='cftools',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://cubefel.netlify.app',
  packages=['tools'],
  install_requires=['requests.txt'],
  keywords='cfPass',
  python_requires='>=9.10'
)