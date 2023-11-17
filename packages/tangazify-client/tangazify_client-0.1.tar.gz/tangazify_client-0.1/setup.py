from setuptools import setup, find_packages

setup(
    name='tangazify_client',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'numpy',
        'opencv-python',
    ],
)
