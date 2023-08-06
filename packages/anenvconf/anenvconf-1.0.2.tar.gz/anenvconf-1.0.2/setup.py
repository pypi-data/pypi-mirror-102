import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="anenvconf",
  version="1.0.2",
  author="anttin",
  author_email="muut.py@antion.fi",
  description="Module for defining a config schema and importing it from environment variables.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/anttin/anenvconf",
  packages=setuptools.find_packages(),
  classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ]
)
