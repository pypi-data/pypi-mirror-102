import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

print(setuptools.find_packages(where="src"))

setuptools.setup(
    name="kublog",
    version="0.0.1",
    author="Chaitanya Nettem",
    author_email="chaitanya@kubric.io",
    description="A logger utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cirbuk/kublog",
    project_urls={
        "Bug Tracker": "https://github.com/cirbuk/kublog/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'contextvars;python_version<"3.7"'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
