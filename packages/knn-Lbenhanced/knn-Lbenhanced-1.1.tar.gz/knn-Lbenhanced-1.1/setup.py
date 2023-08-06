from setuptools import setup, find_packages

setup(
    name='knn-Lbenhanced',
    version='1.1',
    author='Moradisten',
    author_email='moradabaz@gmail.com',
    url='https://github.com/moradisten/KNN-LB',
    keywords='timeseries knn lowerbounds DTW lbEnhanced',
    description="K Nearest Neighbours using LbEnhanced distance measure",
    python_requires='>=3.6',
    packages=find_packages(), install_requires=[
        'matplotlib',
        'dtaidistance',
        'scrapeasy',
        'numpy',
        'scipy'

    ]
)
