import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nma",
    scripts=["scripts/nma"],
    version="0.1",
    author="Jacob Rodal",
    author_email="jr6ff@virginia.edu",
    description="Sends a desktop notification when a process finishes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jrodal98/nma",
    download_url="https://github.com/jrodal98/nma/archive/v0.1.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
