import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdf417decoder-with-opencv-python-headless",
    version="1.0.9",
    author="Sparkfish LLC",
    author_email="packages@sparkfish.com",
    description="A PDF417 barcode decoder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabrielvannier/pdf417decoder-with-opencv-python-headless",
    project_urls={
        "Bug Tracker": "https://github.com/gabrielvannier/pdf417decoder-with-opencv-python-headless",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",    
    install_requires=[
        "numpy >= 1.20.1",
        "opencv-python-headless >= 4.6",
        "pillow >= 9.5.0"
    ],
)