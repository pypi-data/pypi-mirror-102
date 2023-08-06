from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='biobuilder',
    version='0.1.0',
    author='Zhenyu Wei',
    author_email='zhenyuwei99@gmail.com',
    description='BioBuilder is used to create biology model in both all-atom and coarse-grained resolution',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='Biology model builder',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    url='https://openpd.net/en/latest/',
    project_urls={
        "Source Code": "https://github.com/openpd-dev/biobuilder",
    },
    packages=find_packages(),
    package_data={
        "biobuilder": [
            "biobuilder/template/*/*.json"
        ]
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=[
        'numpy',
        'matplotlib',
        'pytest',
        'pytest-xdist',
        'scipy'
    ],
    python_requires='>=3.7'
)
