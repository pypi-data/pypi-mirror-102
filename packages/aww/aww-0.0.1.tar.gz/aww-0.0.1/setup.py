import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aww",
    version="0.0.1",
    author="John Mason",
    author_email="binarymason@users.noreply.github.com",
    description="AWS helper functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/binarymason/aww",
    project_urls={
        "Bug Tracker": "https://github.com/binarymason/aww/issues",
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
