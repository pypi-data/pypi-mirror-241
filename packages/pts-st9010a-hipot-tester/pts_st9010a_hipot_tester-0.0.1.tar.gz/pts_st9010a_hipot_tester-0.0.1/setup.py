from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="pts_st9010a_hipot_tester",
    version="0.0.1",
    author="Pass testing Solutions GmbH",
    description="ST9010A Hipot Tester Driver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="shuparna@pass-testing.de",
    url="https://gitlab.com/pass-testing-solutions/st9010a-hipot-tester",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    py_modules=["pts_st9010a_hipot_tester"],
    install_requires=["pyserial==3.5"],
    packages=find_packages(include=['pts_st9010a_hipot_tester']),
    include_package_data=True,
)
