import os
from setuptools import setup, find_packages
with open(r'.\README.md', 'r', encoding = 'utf-8') as f:
    data = f.read()

setup(
    name='turingAPI-final',
    version='1.0.0',
    description='The API framework for IcodeYoudao.',
    long_description = data,
    long_description_content_type="text/markdown",
    license='MIT Licence',
    project_urls={
        'Homepage': 'https://github.com/xbzstudio/TuringAPI',
        'Documentation': 'https://xbz-studio.gitbook.io/turingapi/'
    },
    author='xbzstudio',
    author_email='mmmhss2022@outlook.com',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.10',
    install_requires=['urllib3>=2.0.7'],
    data_files=[],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Build Tools",
        "Intended Audience :: Developers"
    ],
    scripts=[],
)