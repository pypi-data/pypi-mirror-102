import setuptools

__version__ = "0.0.1"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-roboat-enviro",
    version=__version__,
    author="Drew Meyers",
    author_email="drewm@mit.edu",
    description="Python wrapper for the Roboat Environmental Data REST API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drewmee/py-roboat-enviro",
    license="MIT",
    packages=setuptools.find_packages(exclude=["tests*", "docs"]),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ],
    test_suite="tests",
    install_requires=["uplink>=0.9.4"],
    extras_require={
        "docs": [
            "sphinx>=3.2.0",
            "sphinx-automodapi>=0.12",
            "sphinx-rtd-theme>=0.5.0",
            "msmb_theme>=1.2.0",
            "nbsphinx>=0.7.1",
            "sphinx-copybutton>=0.3.0",
            "black>=20.8b1",
            "isort>=5.4.2",
            "rstcheck>=3.3.1",
        ],
        "tests": ["pytest>=6.0.1", "pytest-dotenv>=0.5.2", "tox>=3.16.1"],
        "develop": ["twine>=3.2.0", "pre-commit>=2.8.2"],
        "jupyter": [
            "ipython>=7.16.1",
            "jupyter>=1.0.0",
            "jupyterlab>=2.2.2",
            "pyeem>=0.2.0",
        ],
    },
)
