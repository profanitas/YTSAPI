import os
import setuptools

def get_long_description():
    with open('README.md', 'r') as f:
        return f.read()

setuptools.setup(
    name="YTSAPI",
    version="0.1.1",
    author="Piyush Raj",
    author_email="piyush@linuxmail.org",
    description="YTSAPI is a python API which allows you to get the transcript/subtitle for a given YouTube video.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="transcribe-api YTSAPI theabuseproject abuse profanity project youtube-api youtube transcript subtitle youtube-subtitle youtube-transcript api",
    url="https://github.com/theabuseproject/YTSAPI",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'requests', 'youtube_dl',
    ],
    entry_points={
        'console_scripts': [
            'ytsapi = ytsapi.__main__:main',
        ],
    },
)
