from setuptools import find_packages, setup

with open ("app/README.md", 'r') as f:
    long_description = f.read()

setup(
    name="hello-func",
    version='0.0.4',
    description="Noway, this prints hello! OMG 360 NOSCOPE MLG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="AlphaPotat",
    author_email="luchinin.n@yandex.ru",
    package_dir={"":"app"},
    packages=find_packages(where="app"),
    url="https://github.com/Alpha-Potat/hello",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "twine", "python-dotenv", "wheel"
        ],
)