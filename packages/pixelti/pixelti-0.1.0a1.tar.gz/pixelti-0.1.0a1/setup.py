from setuptools import setup

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
  name='pixelti',
  version='0.1.0-alpha.1',
  description='A pixel art creation tool',
  url='https://github.com/titancodehub/pixelti',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='titanabrian',
  py_modules=['pixelti'],
)