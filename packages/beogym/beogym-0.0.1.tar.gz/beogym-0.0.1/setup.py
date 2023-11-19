import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="beogym",
    version="0.0.1",
    author="Henghui Bao, Kiran Klekkala",
    author_email="henghuib@usc.edu",  
    description="package for beogym",
    long_description=long_description, 
    long_description_content_type="text/markdown",
    url="https://github.com/DrokBing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

