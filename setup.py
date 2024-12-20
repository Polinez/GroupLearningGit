import os
from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

version = os.getenv(
    "VERSION",
    "0.0.0",  # gets version from virtual envirements with is setup in deploymentCD.yml
)

setup(
    name="GroupLearningGit",
    version=version,  # version from virtual envirement
    author="Sebastian Wandzel",
    author_email="sebastianwandzel@yahoo.pl",
    description="Aplication to menage students attendance",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Polinez/GroupLearningGit",
    packages=find_packages(),  # auto finding packages
    install_requires=required_packages,  # requirements from requirements.txt
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Teachers",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
    entry_points={
        "console_scripts": [
            "menageStudents=src.task1:main",  # script when someone uses menageStudents in console he can run this app
        ]
    },
)
