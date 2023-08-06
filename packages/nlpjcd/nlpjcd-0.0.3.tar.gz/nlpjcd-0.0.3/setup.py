import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nlpjcd",
    version="0.0.3",
    author="Juan Camilo Diaz",
    author_email="juancadh@gmail.com",
    description="NLP Toolkit Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juancadh/nlpjcd",
    project_urls={
        "Bug Tracker": "https://github.com/juancadh/nlpjcd/issues",
    },
    keywords='nlp, ner, toolkit',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    package_data={
        'entities': ['nlp_jcd_entities.json'],
    },
)