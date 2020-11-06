from setuptools import setup, find_packages

setup(name = 'MyStoreAPITest',
      version='1.0',
      description='Practice API testing',
      author='Manish Saini',
      email='manishsaini74.ms@gmail.com',
      packages=find_packages(),
      install_requires=[
            "pytest==",
            "pytest-html==",
            "requests==",
            "requests-oauthlib==",
            "PyMySQL==",
            "WooCommerce==",
            ]
      )