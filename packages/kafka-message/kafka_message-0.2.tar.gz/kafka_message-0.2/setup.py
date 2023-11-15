from setuptools import setup, find_packages

setup(
    name='kafka_message',
    version='0.2',
    summary="",
    author="hoatv9",
    license='MIT',
    description="Test",
    packages=find_packages(),
    install_requires=[
        'kafka-python'
    ],
)