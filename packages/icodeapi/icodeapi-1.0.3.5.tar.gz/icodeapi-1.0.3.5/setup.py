import os
from setuptools import setup, find_packages
with open(r'.\README.md', 'r', encoding = 'utf-8') as f:
    data = f.read()

setup(
    name='icodeapi',
    version='1.0.3.5',
    description='The second generation of IcodeYoudao API framework.',
    long_description = data,
    long_description_content_type="text/markdown",
    license='MIT Licence',
    project_urls={
        'Homepage': 'https://github.com/xbzstudio/icodeapi',
        'Documentation': 'https://xbzstudio.github.io/_book/'
    },
    author='xbzstudio',
    author_email='mmmhss2022@outlook.com',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.10',
    install_requires=['httpx>=0.25.0', 'aiofiles>=23.2.1', 'urllib3>=2.0.7'],
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