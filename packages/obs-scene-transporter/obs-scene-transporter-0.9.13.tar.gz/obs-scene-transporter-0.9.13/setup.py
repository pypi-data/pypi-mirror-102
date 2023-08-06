import os
import setuptools
import subprocess

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="obs-scene-transporter",
    use_scm_version=True,
    author="Stefan Bethke",
    author_email="stb@lassitu.de",
    description="Import and export OBS Studio scenes including all assets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stblassitude/obs-scene-transporter",
    project_urls={
        "Bug Tracker": "https://github.com/stblassitude/obs-scene-transporter/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['obs-scene-transporter=obsscenetransporter:main']
    },
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
    setup_requires=['setuptools_scm'],
)