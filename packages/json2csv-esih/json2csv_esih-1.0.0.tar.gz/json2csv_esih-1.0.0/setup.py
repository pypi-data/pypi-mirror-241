from setuptools import setup, find_packages

setup(
    name='json2csv_esih',
    version='1.0.0',
    description='Convert JSON to CSV',
    author='Py0095 & Rubenson',
    packages=find_packages(),  
    install_requires=[],  
    author_email="pyp0859@gmail.com",
    entry_points={ 
        'console_scripts': [
            'json2csv = json2csv.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
