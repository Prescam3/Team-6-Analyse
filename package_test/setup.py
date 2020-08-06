from setuptools import setup, find_packages

setup(
    name='test',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/prescam3@gmail.com',
    author='Presca Mashamaite',
    author_email='prescam3@gmail.com'
)