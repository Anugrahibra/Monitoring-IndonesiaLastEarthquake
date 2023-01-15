import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Monitoring-IndonesiaLastEarthquake",
    version="0.0.2",
    install_requires=[
        'beautifulsoup4',
        'requests'
    ],
    author="Anugrah Ibra",
    author_email="anugrahibra88@gmail.com",
    description="This package will get the latest earthquake from "
                "Indonesia Meteorological, Climatological, and Geophysical Agency (BMKG).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Anugrahibra",
    project_urls={
        "Medium": "https://medium.com/@anugrahibra88",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)