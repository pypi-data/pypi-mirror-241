from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='fakenamegenerator',
    version='0.1.0',
    author="Vetochka",
    author_email="vetochka@ulis.family",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
	install_requires=[
        "requests",
		"bs4",
	],
    description="Very mimimalistic unofficial python API for fakenamegenerator.com",
    long_description=long_description,
    long_description_content_type='text/markdown',
)
