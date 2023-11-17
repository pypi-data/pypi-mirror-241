from setuptools import setup, find_packages

setup(
    name='KernelAVO',
    version='0.1',
    packages=find_packages(),
    description='Curve fitting for COVID-19 data using three different kernels',
    author='Alejandro Valencia',
    author_email='alejandro.valenciao1@udea.edu.co',
    license="MIT",
    install_requires=['numpy','pandas', 'matplotlib'],
)
