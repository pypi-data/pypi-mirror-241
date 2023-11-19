import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DiscSelfEasy",
    version="0.2",
    author="Cybreak",
    author_email="cybreak@cybreak.dev",
    description="Makes discord self boting easy!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cybreak/Disc-Self-Easy/tree/main",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)