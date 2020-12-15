import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="punny-poetry", # Replace with your own username
    version="0.0.1",
    author="Punny Poets",
    author_email="author@example.com",
    description="A python package that generates punny limericks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ezosa/punny-poetry",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)