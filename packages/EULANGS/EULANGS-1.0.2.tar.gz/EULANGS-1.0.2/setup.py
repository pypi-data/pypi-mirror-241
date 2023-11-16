import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
	name="EULANGS",
	version="1.0.2",
	author="Simon Hengchen",
	author_email="simon@iguanodon.ai",
	description="This package allows you to import a list of official EU languages.",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	license = "GNU General Public License v3 (GPLv3)",
    url = "https://github.com/iguanodon-ai/EULANGS",
	classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    #package_dir = {"": ".EULANGS"},
    packages = setuptools.find_packages(where="."),
    python_requires = ">=3.6"
)
