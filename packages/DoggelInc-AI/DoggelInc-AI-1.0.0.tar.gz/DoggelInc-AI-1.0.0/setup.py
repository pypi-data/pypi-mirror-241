from setuptools import setup, find_packages

setup(
    name='DoggelInc-AI',  # Replace with your package name
    version='1.0.0',  # Replace with your package version
    description='Doggeł Inc AI package for request to make ppls life easier',
    author='Lordpomind',
    author_email='lordpomind@gmail.com',
    url='',  
    packages=find_packages(),  
    install_requires=[  # List your package dependencies here
        'aiohttp'      
    ],
    classifiers=[  
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',        
        'Programming Language :: Python :: 3.10',        
        'Programming Language :: Python :: 3.11',
    ],
)
