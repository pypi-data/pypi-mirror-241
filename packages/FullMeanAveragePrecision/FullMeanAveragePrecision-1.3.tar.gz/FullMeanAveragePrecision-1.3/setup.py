from setuptools import setup
from glob import glob

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(name='FullMeanAveragePrecision',
      version='1.3',
      description='Expanded version MeanAveragePrecision metric torchmetrics library',
      packages=['FullMeanAveragePrecision'],
      author_email='efremov.va@phystech.edu',
      install_requires=[
            'torch', 'torchmetrics', 'pycocotools',
      ],
      data_files=[(("assets"), glob("assets/*"))],
      author="Vlad Efremov",
      long_description=long_description,
      long_description_content_type="text/markdown",
      zip_safe=False)
