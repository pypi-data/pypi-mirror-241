import setuptools
import os

def get_version():
    version_file = 'npp_materialslab_tools/__init__.py'
    with open(version_file, 'r') as file:
        for line in file:
            if line.startswith('__version__'):
                # Extract the version number
                version = line.split('=')[1].strip().strip('\'"')
                return version
    raise RuntimeError('Cannot find version information')

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = [
    #'opencv',
    'scipy',
    'numpy',
    'matplotlib',
    'seaborn',
    'pandas',
    'openpyxl',
    'ipykernel',
    'jupyter'
 ]

test_requirements = [
    'pytest',
    # 'pytest-pep8',
    # 'pytest-cov',
]


setuptools.setup(
    name="npp_materialslab_tools", # Replace with your own username
    version=get_version(),
    author="N. Papadakis",
    author_email="npapnet@gmail.com",
    description="A package for the material lab tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    tests_require=test_requirements,
    python_requires='>=3.8',
    project_urls={
        'Documentation': 'https://npapnet.github.io/hmu.materialslab.tools/',
        'Source': 'https://github.com/npapnet/hmu.materialslab.tools'
    },
    
)