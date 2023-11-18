from setuptools import find_packages, setup

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
  name='pixelti',
  version='0.1.0a4',
  description='A pixel art creation tool',
  url='https://github.com/titancodehub/pixelti',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='titanabrian',
)