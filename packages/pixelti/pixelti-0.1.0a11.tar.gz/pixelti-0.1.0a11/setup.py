from setuptools import setup

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

if __name__ == '__main__':
  setup(package = ['pixelti'], install_requires=requirements, include_package_data=True)
