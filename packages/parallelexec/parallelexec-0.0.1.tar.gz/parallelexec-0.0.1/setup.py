from setuptools import setup

with open("README.md") as f:
    markdown_description = f.read()

setup(
    name="parallelexec",
    version="0.0.1",
    author="ashgw",
    url="https://github.com/AshGw/parallelexec.git",
    description="Utility module that provides convenient decorators and functions to parallelize the execution of functions",
    long_description_content_type="text/markdown",
    long_description=markdown_description,
    python_requires=">=3.10",
    package_data={
        "parallelexec": ["**"],
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
)
