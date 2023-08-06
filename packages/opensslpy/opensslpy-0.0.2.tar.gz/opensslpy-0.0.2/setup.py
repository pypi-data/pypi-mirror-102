import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opensslpy",
    version="0.0.2",
    author="Madhava-mng",
    author_email="alformint@gmail.com",
    description="run openssl via python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Madhava-mng/openssltool",
    packages=setuptools.find_packages(),
    project_urls={
        "Bug Tracker": "https://github.com/Madhava-mng/openssltool",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

