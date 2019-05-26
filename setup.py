import setuptools

with open("README.MD", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_arcade_menu",
    version="0.0.1",
    author="akapkotel",
    autor_email="btcuserbtc@gmai.com",
    desription="simple menu classes for use in Arcade library projects",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Share Alike Attribution-NonCommercial-ShareAlike 4.0",
        "Operating System :: OS Independent",
    ],
)