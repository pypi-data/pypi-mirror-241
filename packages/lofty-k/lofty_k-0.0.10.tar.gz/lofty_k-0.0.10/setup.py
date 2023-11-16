from setuptools import find_packages, setup


setup(
    name="lofty_k",
    version="0.0.10",
    description="hand",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description="",
    long_description_content_type="text/markdown",
    url=" ",
    author="M0F0IAm",
    author_email=" ",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    }
)