import setuptools

with open("README", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PingF", # Replace with your own PyPI username(id)
    version="1.0.2",
    author="PingF",
    author_email="ping01@ruu.kr",
    description="SSHI AH !",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)