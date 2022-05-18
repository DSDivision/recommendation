from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="DSDivision-recommendation",
    version="1.0.0",
    description="A simple movie recommendation website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DSDivision/recommendation",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        'FastAPI[all]',
        'pandas'
    ]
)