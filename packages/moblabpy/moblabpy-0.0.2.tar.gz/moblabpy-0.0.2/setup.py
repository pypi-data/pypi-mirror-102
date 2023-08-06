import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moblabpy", # Replace with your own username
    version="0.0.2",
    author="Moblabpy Official",
    author_email="moblabpy@gmail.com",
    description="A module that allow users to stimluate communcation system via their own device",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moblabpy/moblabpy",
    project_urls={
        "Code": "https://github.com/moblabpy/moblabpy",
        "Documentation": "https://moblabpy.readthedocs.io/en/latest/",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Communications",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords = ["BYOD", "COMMUNICATION"],
    install_requires=[
        'numpy',
        'segno',
        'pyzbar',
        'Pillow',
        'opencv-python',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)