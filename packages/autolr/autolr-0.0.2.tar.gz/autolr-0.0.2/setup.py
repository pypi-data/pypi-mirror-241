import pathlib
import setuptools

setuptools.setup(
    name="autolr",
    version="0.0.2",
    description="A simple package for automatic logistic regression",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Ayush Pratap Singh",
    author_email="ayushpsingh113@gmail.com",
    project_urls={
        "Source": "https://github.com/ayushpratap113/autolr",
    },
    classifiers=["Programming Language :: Python :: 3.9",
                 "License :: OSI Approved :: MIT License",
                 "Intended Audience :: Information Technology",
                 "Operating System :: OS Independent",
                 "Topic :: Scientific/Engineering :: Artificial Intelligence"],
    python_requires='>=3.8',
    install_requires=["numpy>=1.21.2",
                      "pandas>=1.4.2",
                      "scikit-learn",
                      "imbalanced-learn>=0.11.0"],
    packages=setuptools.find_packages(),
    include_package_data=True,


)