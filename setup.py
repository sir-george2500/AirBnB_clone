from setuptools import setup, find_packages

setup(
    name='Airbnb_console',
    version='0.1',
    author='George S Mulbah',
    description='A console application for Airbnb',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your project may have
    ],
    entry_points={
        'console_scripts': [
            'airbnb_console = airbnb_console.main:main',
        ],
    },
)
