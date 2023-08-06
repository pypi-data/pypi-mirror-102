import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def _setup():
    setuptools.setup(
        name="penitus",
        version="1.1",
        description="Shows information about cryptocurrencies, like prices.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="MIT",
        author="Gino Zanella",
        author_email="iosgino@hotmail.com",
        readme="README.md",
        url="https://github.com/fckvrbd/penitus",
        install_requires=["requests"],
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src"),
        python_requires=">3.0",
        keywords=[
            "Cryptocurrency",
            "Finances",
            "Bitcoin",
            "Coinpaprika",
            "Investing"
        ],
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Development Status :: 4 - Beta",
            "Natural Language :: English",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Topic :: Software Development",
            "Topic :: Office/Business :: Financial :: Investment",
        ],
    )


if __name__ == "__main__":
    _setup()
