from setuptools import setup, find_packages

setup(
    name='dynamo_db_py',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'schema==0.7.5',
        'boto3==1.28.27'
    ]
)
