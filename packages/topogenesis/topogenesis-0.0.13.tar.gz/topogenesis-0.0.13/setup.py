from setuptools import setup, find_packages

setup(name='topogenesis',
      version='0.0.13',
      description='Topological Structures and Methods for Generative Systems and Sciences',
      url='https://github.com/shervinazadi/topoGenesis',
      author='Shervin Azadi, and Pirouz Nourian',
      author_email='shervinazadi93@gmail.com',
      
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      python_requires='>=3.7',
      include_package_data=True,
      install_requires=[
    'numpy',
    'pandas',
    # any other dependencies
],
      )
