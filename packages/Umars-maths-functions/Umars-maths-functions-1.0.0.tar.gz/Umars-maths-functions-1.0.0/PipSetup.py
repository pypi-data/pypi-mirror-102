import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Umars-maths-functions",
    version="1.0.0",
    description="Functions from Umar's maths stuff. Use to create things!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://www.loom.com/share/e7a3212ec2af446c81699a7f9109135f",
    author="Umar Sharief",
    author_email="umar.sharief04@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude='README.md'),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "maths-functions=functions.__main__:main",
        ]
    },
)