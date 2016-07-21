from setuptools import setup

def readme():
    return open('./README.rst').read()

setup(name='luhnmod10',
      version='1.0.2',
      description='A fast and simple in-place implementation of the luhn check algorithm.',
      long_description=readme(),
      url='https://github.com/luhnmod10/python',
      author='Leigh McCulloch',
      license='MIT',
      packages=['luhnmod10'],
      zip_safe=True,
      )
