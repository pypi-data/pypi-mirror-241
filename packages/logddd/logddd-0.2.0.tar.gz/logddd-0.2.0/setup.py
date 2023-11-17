import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="logddd",
    version="0.2.0",
    author="LinFeng Dai",
    author_email="dailinfeng66@163.com",
    description="print python logddd",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dlfld/py-simple-log",
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
