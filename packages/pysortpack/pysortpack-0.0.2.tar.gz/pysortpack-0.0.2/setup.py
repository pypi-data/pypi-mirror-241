from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="pysortpack",
    version="0.0.2",
    description="A package to perform different types Sorting algorithms.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/J0schu/pysortpack",
    author="J0schu",
    license="MIT",
    keywords=["sort", "sorting"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)