from pathlib import Path

from setuptools import setup

setup(
    name="tbomber",
    version="0.5",
    author_email="pulsar04040@gmail.com",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/tulen34/tbomber",
    packages=["tbomber"],
    license="MIT",
    install_requires=["click", "httpx"],
    python_requires=">=3.9",
)
