from setuptools import setup, find_packages  # type: ignore


setup(
    name="laity_data_structures",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[],
    description="Data Structure Package By Pappalaity",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Pappa laity",
    author_email="pappalaity@gmail.com",
    url="https://github.com/PappaLaity/pappa-laity-data-structures-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
