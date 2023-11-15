import setuptools

setuptools.setup(
    name="mapleapi",              
    version="1.1.0",
    author="HYG_Studio",
    author_email="hygstudio@hyhbx.com",
    long_description="Please come to https://docs.mapleapi.net Check out the documentation,Thank you",
    description="Python package for Mapleapi",
    url="https://docs.mapleapi.net/pack/pypi",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests'
    ],
    python_requires='>=3',
)