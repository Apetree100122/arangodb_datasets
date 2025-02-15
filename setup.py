from setuptools import setup, find_packages

setup(
    name='arangodb_datasets',
    version='0.1.0',
    description='Implementation of SFTP for ArangoDB Datasets',
    author='alexander petree',
    author_email='apetree1001@email.phoenix.edu',
    url='https://github.com/Apetree100122/arangodb_datasets',
    packages=find_packages(),
    install_requires=[
        'requests',
        'arango'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
