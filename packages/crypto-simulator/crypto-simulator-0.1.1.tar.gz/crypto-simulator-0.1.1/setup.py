from setuptools import setup

setup(
    name='crypto-simulator',
    version='0.1.1',
    packages=['src'],
    install_requires=[
        'ccxt==4.1.50',
        'matplotlib==3.8.1',
        'pandas==2.1.3',
        'tk==0.1.0',
    ],
    entry_points={
        'console_scripts': [
            'crypto-simulator = src:main',
        ],
    },
    author='Max Paul',
    author_email='maxkpaul21@gmail.com',
    description='A crypto trading simulator',
    url='https://github.com/max-paul/crypto-simulator',
)