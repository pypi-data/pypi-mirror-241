from setuptools import setup, find_packages

setup(
    name='Cloudimate',
    version='0.1',
    packages=find_packages(),       
    install_requires=[
        'click',
        'keyring',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'cm=cm.cm:cm',
        ],
    },
)
