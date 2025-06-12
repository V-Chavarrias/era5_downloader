from setuptools import setup, find_packages

setup(
    name='era5_downloader',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'cdsapi',
    ],
    author='Victor Chavarrias',
    description='ERA5 data downloader using CDS API',
    url='https://github.com/yourusername/era5_downloader',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
