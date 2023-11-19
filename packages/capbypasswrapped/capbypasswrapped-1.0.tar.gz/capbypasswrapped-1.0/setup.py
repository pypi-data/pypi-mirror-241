from setuptools import setup, find_packages

setup(
    name='capbypasswrapped',
    version='1.0',
    packages=find_packages(),
    setup_requires=['setuptools_scm', 'wheel'],
    install_requires=[
        'requests',
        'logging'
    ],
)