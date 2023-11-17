from setuptools import setup, find_packages


setup(
    name='mitali-package',
    version='1.2',
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
