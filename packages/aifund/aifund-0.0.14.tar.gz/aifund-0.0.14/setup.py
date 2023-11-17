import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aifund",
    version="0.0.14",
    author="tiano",
    author_email="silence_hgt@163.com",
    description="AIfund 是基于 Python 的基金量化工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/silenceTiano/aifund",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
