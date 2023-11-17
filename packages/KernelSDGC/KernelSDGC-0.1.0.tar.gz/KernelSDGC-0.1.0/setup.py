from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    description_l=fh.read()

setup(
    name='KernelSDGC',
    version='0.1.0',
    packages=find_packages(include=['KernelSDGC']),
    description='KernelSDGC',
    long_description=description_l,
    long_description_content_type='text/markdown', 
    author='Sebastian Diaz Granados Cano',
    license='MIT',
    install_requires=['matplotlib==3.8.1', 'pandas==2.1.2', 'numpy==1.26.1'],
    python_requires= '>=3.10.12',
    author_email='sebasdgc14@gmail.com',
    url='https://gitlab.com/sebasdgc14/personal'
    )