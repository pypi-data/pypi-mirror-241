from setuptools import setup, find_packages

setup(
    name='schedule-sdk',
    version='0.2.9',
    packages=find_packages(),
    install_requires=[
        "requests",
        "redis"
    ],
)