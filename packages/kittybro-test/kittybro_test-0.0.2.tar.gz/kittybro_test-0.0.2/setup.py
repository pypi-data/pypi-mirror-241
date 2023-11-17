from setuptools import setup, find_packages

setup(
    name="kittybro_test",
    version="0.0.2",
    author="kitty bro",
    author_email="exmaple@gmail.com",
    description="kittybro package brings you happiness",
    long_description="it's just a test of kitty bro package",
    long_description_content_type="text/markdown",
    url="https://github.com/ehrlichsei/pypi_test.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
