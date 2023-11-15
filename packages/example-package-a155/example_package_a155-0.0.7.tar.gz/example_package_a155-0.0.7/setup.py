from setuptools import setup, find_packages

setup(
    name='example_package_a155',
    version='0.0.7',
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your package',
    packages=find_packages(),
    install_requires= ['web3', 'ipfshttpclient==0.8.0a2','requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)