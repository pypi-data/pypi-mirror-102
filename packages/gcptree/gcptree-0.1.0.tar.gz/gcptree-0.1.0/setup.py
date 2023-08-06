from setuptools import setup

setup(name='gcptree',
      version='0.1.0',
      description='List your GCP Org heirachy as a tree in JSON or Text',
      url='http://github.com/onetwopunch/gcptree',
      scripts=['bin/gcptree'],
      author='Ryan Canty',
      author_email='onetwopunch@pm.me',
      license='MIT',
      packages=['gcptree'],
      zip_safe=False,
      install_requires=[
        "deepmerge==0.2.1",
        "google-api-python-client==1.12.8",
        "colorama==0.4.3",
      ])