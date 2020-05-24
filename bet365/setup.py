import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bet365",
    version="0.0.3",
    author="William Batista",
    author_email="ninja25538@tutanota.de",
    description="ninja25538@tutanota.de",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/billyb2/bet365-scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.6',
)