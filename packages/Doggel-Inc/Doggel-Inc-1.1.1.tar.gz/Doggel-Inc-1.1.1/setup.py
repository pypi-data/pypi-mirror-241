from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Doggel-Inc",
    version="1.1.1",
    author="Lordpomind",
    author_email="lordpomind@gmail.com",
    description="A package with all Doggeł Inc services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    packages=find_packages(),
    url="https://github.com/Lordpomind0001/DIAI",
    install_requires=[

        "aiohttp",
    ],
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)