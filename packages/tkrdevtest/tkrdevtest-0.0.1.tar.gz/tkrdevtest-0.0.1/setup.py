import pathlib
import setuptools

setuptools.setup(
  name="tkrdevtest",
  version="0.0.1",
  author="tkr.",
  author_email="toolkitr.email@gmail.com",
  description="Testing toolkitr.",
  long_description=pathlib.Path("README.md").read_text(),
  long_description_content_type="text/markdown",
  url="https://github.com/toolkitr/tkrdisc",
  packages=setuptools.find_packages(),
  include_packge_data=True,
  classifiers=[
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "License :: OSI Approved :: MIT License",
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
  ],
  python_requires=">=3.10,<3.12",
  entry_points={
    "console_scripts": [
      "tkrdevtest=tkrdevtest.__main__:main"
    ],
  },
  
  
)