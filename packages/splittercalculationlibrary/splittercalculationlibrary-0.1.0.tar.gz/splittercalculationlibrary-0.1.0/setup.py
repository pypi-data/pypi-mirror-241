from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="splittercalculationlibrary",
    version="0.1.0",
    author="Soorya",
    author_email="jeyasooryamanoharan@gmail.com",
    description="A simple calculation for the Splitwise application",
    long_description=long_description,
    url="",
    packages=find_packages(),
    keywords='splittercalculation',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # add any dependencies required by your package here
    ],
)
