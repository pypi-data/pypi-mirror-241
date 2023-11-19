from setuptools import setup, find_packages

setup(
    name='schedule-sdk',
    version='0.3.6',
    packages=find_packages(),
    install_requires=[
        "requests",
        "redis"
    ],
)