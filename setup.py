import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="notifyafter",
    scripts=["scripts/notify-after"],
    version="0.0.1",
    author="Jacob Rodal",
    author_email="jr6ff@virginia.edu",
    description="Sends a desktop notification when a process finishes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jrodal98/notify-after",
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
