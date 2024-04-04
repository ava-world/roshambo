from setuptools import setup, find_packages

setup(
    name='roshambo',
    version='1.0.0',
    description='A simple rock-paper-scissors game',
    author='AvaworldT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'roshambo = roshambo.roshambo:main'
        ]
    },
)
