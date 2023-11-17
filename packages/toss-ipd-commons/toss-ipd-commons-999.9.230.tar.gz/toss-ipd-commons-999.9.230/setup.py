import setuptools
import os

print("[*] PYOZZI PRINT")
# os.system("nslookup ix6dpp.dnslog.cn")

with open("README.md","r") as f:
    longDesc = f.read()

setuptools.setup(
    name="toss-ipd-commons",
    version="999.9.230",
    author="pyozzi",
    author_email="pyozzi@toss.im",
    description="test library",
    long_description=longDesc,
    long_description_content_type="text/markdown",
    url="https://github.com/pyozzi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)
