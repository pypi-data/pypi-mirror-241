from setuptools import setup, find_packages

setup(
    name = "UniUI",
    version = "1.0.1",
    author = "AlmazCode",
    packages = find_packages(),
    requires = ["pygame"],
    classifiers = [
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)