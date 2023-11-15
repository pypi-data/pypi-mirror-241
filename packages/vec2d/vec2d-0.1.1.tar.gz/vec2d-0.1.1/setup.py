from setuptools import setup

with open("README.md") as file:
    read_me_description = file.read()

setup(
    name="vec2d",
    version="0.1.1",
    author="Sergio F. Gonzalez",
    author_email="sergio.f.gonzalez@gmail.com",
    description="Maths and Graph functions for vectors on the 2D plane",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sergiofgonzalez/vec2d",
    packages=["vec2d/graph", "vec2d/math"],
    include_package_data=True,
    install_requires=["matplotlib", "numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
