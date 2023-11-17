from setuptools import setup, find_packages


setup(
    name='mitali_package',
    version='1.1',
    license='MIT',
    author="Mitali Bisht",
    author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)
