import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylfgp",                     # This is the name of the package
    version="0.0.2",                        # The initial release version
    author="Qi Xu, Arlina Shen, and Annie Qu",                     # Full name of the author
    description="Python package for Crowdsourcing using Latent Factor model with subGroup Penalty (LFGP)'",
    long_description="Implement the method in the paper 'Crowdsourcing Utilizing Subgroup Structure of Latent Factor Modeling.'",      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["pylfgp"],             # Name of the python package
    package_dir={'':'pylfgp/src'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)