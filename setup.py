import os
import setuptools

def get_long_description():
    with open('README.md', 'r') as f:
        return f.read()

setuptools.setup(
    name="YTAPI",
    version="0.1.0",
    author="Piyush Raj",
    author_email="piyush@linuxmail.org",
    description="YTAPI is a python API which allows you to get the transcript/subtitle for a given YouTube video.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="transcribe-api ytapi theabuseproject abuse profanity project youtube-api youtube transcript subtitle youtube-subtitle youtube-transcript api",
    url="https://github.com/theabuseproject/ytapi",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'ytapi = ytapi.__main__:main',
        ],
    },
)
