from setuptools import setup

setup(name='FullMeanAveragePrecision',
      version='1.0',
      description='Expanded version MeanAveragePrecision metric torchmetrics library',
      packages=['FullMeanAveragePrecision'],
      author_email='efremov.va@phystech.edu',
      install_requires=[
            'torch', 'torchmetrics', 'pycocotools',
      ],
      zip_safe=False)