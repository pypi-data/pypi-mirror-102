import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pkgpy", # Replace with your own username
    version="0.0.2",
    scripts=['pkg.py'],
    author="Sakurai07",
    author_email="blzzardst0rm@Gmail.com",
    description="Cross platform cross language package manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eris9/pkgpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)