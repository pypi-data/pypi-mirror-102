import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ndmath",
    version="0.0.4",
    author="Esteban L. Castro-Feliciano",
    author_email="ecastro@crown-hydro.com",
    description="N-dimensional complex step and finite step differentiation, and Newton's method.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elcf/python-ndmath",
    project_urls={
        "Bug Tracker": "https://github.com/elcf/python-ndmath/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["ndmath"],
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=[
        'numpy',
    ],
)
