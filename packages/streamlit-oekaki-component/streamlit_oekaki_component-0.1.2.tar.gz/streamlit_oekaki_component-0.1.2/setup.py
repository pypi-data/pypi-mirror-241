from setuptools import setup, find_packages

setup(
    name="streamlit_oekaki_component",
    version="0.1.2",
    author="Gohei Kusumi",
    author_email="gohei.kusumi@gmail.com",
    description="A Streamlit component for simple freehand drawing. It allows users to draw freely on a canvas and integrates seamlessly with Streamlit apps.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Gohei/streamlit_oekaki_component",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
