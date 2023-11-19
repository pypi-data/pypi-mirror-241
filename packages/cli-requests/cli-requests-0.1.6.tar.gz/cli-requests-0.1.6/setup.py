import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="cli-requests",
    version="0.1.6",
    description="simple cli program to send requests",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Sabberian/cli_requests",
    author="sabberian",
    license="MIT",
    entry_points={
        'console_scripts': [
            'cli-requests=cli_requests.__main__:main',
        ],
    },
    python_requires='>=3.8',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests==2.31.0',
        'colorama==0.4.6',
    ],
)