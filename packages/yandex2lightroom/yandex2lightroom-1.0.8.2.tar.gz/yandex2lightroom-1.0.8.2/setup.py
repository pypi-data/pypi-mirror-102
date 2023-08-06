from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '1.0.8.2'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


install_requires = [
    "beautifulsoup4>=4.8.0, <5.0",
    "certifi>=2020.12.5, <2021",
    "chardet>=3.0.4, <4.0",
    "dataclasses>=0.6, <1.0",
    "dataclasses-json>=0.2.14, <1.0",
    "idna>=2.8, <3.0",
    "lxml>=4.6.2, <5.0",
    "marshmallow>=3.0.0rc6, <4.0",
    "marshmallow-enum>=1.5.1, <2.0",
    "mypy-extensions>=0.4.3, <1.0",
    "requests>=2.22.0, <3.0",
    "selenium>=3.141.0, <4.0",
    "selenium-wire>=2.1.2, <3.0",
    "soupsieve>=2.1, <3.0",
    "stringcase>=1.2.0, <2.0",
    "typing>=3.7.4, <4.0",
    "typing-extensions>=3.7.4.3, <4.0",
    "typing-inspect>=0.6.0, <1.0",
    "urllib3>=1.25.3, <2.0"
]

setup(
    name='yandex2lightroom',
    packages=['yandex2lightroom'],
    version=__version__,
    license='MIT',
    description="Python Script to download images from Yandex.Images for the use in Adobe Lightroom.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Dieter Stockhausen',
    author_email='dieter@schwingenhausen.at',
    url='https://github.com/sto3014/yandex2lightroom-git',
    download_url=f'https://github.com/sto3014/yandex2lightroom-git/archive/main.zip',
    keywords='yandex images download save terminal command-line scrapper lightroom',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        "console_scripts": [
            'yandex2lightroom = yandex2lightroom:run_main'
        ]
    }
)
