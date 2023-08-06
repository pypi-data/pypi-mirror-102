import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pkg-Sakurai07", # Replace with your own username
    version="0.0.1",
    author="Sakurai07",
    author_email="blzzardst0rm@gmail.com",
    description="A package manager for all platforms and 20+ languages by eris9/sakurai07",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eris9/pkgpy",
    project_urls={
        "Bug Tracker": "https://github.com/eris9/pkgpy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)