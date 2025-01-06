from setuptools import setup, find_packages

setup(
    name="JTRFaker",
    version="1.1.0",
    author="Leander Cain Slotosch",
    author_email="slotosch.leander@outlook.de",
    description="A library to generate fake data for various use cases",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LeanderCS/JTRFaker",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "SQLAlchemy>=1.3",
        "Faker>=10.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
