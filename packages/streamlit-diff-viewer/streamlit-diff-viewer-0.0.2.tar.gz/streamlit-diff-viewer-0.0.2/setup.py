import setuptools
from pathlib import Path

setuptools.setup(
    name="streamlit-diff-viewer",
    version="0.0.2",
    author="Quentin Febvre",
    author_email="quentin.febvre@gmail.com",
    description="A simple component to view diff between to files",
    long_description=Path('../README.md').read_text(),
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
