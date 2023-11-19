from setuptools import setup

VERSION = "0.0.1"
DESCRIPTION = "MerkleTree implementation"
LONG_DESCRIPTION = "Yet another package for MerkleTree, compatible with OpenZeppelin implementation"

setup(
    name="merkle-zeppelin",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="akcelero",
    author_email="akcelero@gmail.com",
    license="MIT",
    packages=[],
    url="https://github.com/akcelero/merkle-zeppelin",
    keywords="merkle tree merkletree openzeppelin",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
    ],
)
