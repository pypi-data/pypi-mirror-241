import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# with open("requirements.txt", "r", encoding="utf-8") as f:
#     requirements = f.read().split("\n")

setuptools.setup(
    name="kadita",
    version="0.0.12",
    author="Firza Ichlasul Amal Ariansyah",
    author_email="napija25@gmail.com",
    description="Kadita Computer Vision",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Specify it's Markdown format
    url="https://github.com/Kastara-Digital-Technology/KaditaCV",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["kadita = kadita.DeepFace:cli"],
    },
    python_requires=">=3.5.5",
)
