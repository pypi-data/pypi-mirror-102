from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "A simple package to lookup information via DOI"

setup(
    name="doi_lookup",
    version=VERSION,
    author="Tahir Murata",
    author_email="<tahirmurata83@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=["requests"],

    keywords=["python", "doi", "sci-hub", "scihub", "science", "article", "paper"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)