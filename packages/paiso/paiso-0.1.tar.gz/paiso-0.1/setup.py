import pathlib
import setuptools

setuptools.setup(
    name="paiso",
    version="0.1",
    description="Example to build paiso",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="RAKOTONIAINA Harry Yves",
    author_email="iharrysh.rakotoniaina@gmail.com",
    license=pathlib.Path("LICENSE").read_text(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities",
    ],
    python_requires=">=3.10, <3.12",
    packages=setuptools.find_packages(),
    include_package_data=True,
)
