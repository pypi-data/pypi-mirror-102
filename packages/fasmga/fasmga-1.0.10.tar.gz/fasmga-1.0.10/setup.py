import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fasmga",
    version="1.0.10",
    author="ParliamoDiPC",
    author_email="developer@fasm.ga",
    description="Python Fasm.ga API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fasm-ga/fasmga-python-wrapper",
    project_urls={
        "Bug Tracker": "https://github.com/fasm-ga/fasmga-python-wrapper/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'src': "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)