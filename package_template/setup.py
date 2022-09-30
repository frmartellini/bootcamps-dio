from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing",
    version="0.0.1",
    author="your_name",
    author_email="xxxx@email.com",
    description="Image Processing Package",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="url_for+_my_github",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)