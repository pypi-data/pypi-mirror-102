from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='tiffanyke-aquastat',  

    version='1.0.7', 
  
    description='Python package for MSIA 423 Assignment 1',  
    long_description=long_description, 
    long_description_content_type='text/markdown',
  
  
    url='https://github.com/tiffanyke888/2021-msia423-Ke-Tiffany-assignment1', 
    author='Tiffany Ke', 
    author_email='tiffanyke2021@u.northwestern.edu', 

    packages=find_packages(where='src'), 
    package_dir={'': 'src'},

    python_requires='>=3.6, <4',
    install_requires=['pandas','seaborn','numpy'],


    extras_require={
      'dev': ['matplotlib'],
      'test': ['pytest']
      },

    package_data={  
        'tke_aquastat': ['aquastat.csv.gzip'],
    },


)
