from distutils.core import setup
from setuptools import find_packages

setup(
      name = 'PyLogger',
      version='1.0',
      author='Tarun',
      author_email='ks.tarun@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      url='https://github.com/tarun-singhal/PyLogger',
      licence='',
      description='',
      long_description='',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Scientific/Engineering :: GIS',
    ],
    zip_safe=FALSE 
)

