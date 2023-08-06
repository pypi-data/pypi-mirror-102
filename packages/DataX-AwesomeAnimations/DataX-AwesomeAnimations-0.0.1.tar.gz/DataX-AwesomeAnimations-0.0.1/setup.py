import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DataX-AwesomeAnimations", # Replace with your own username
    version="0.0.1",
    author="AwesomeAnimations",
    author_email="None@sorry.com",
    description="Awesome and easy to use database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AwesomeAnimations/dataxbugs",
    project_urls={
        "Bug Tracker": "https://github.com/AwesomeAnimations/dataxbugs",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)