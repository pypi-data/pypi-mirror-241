from setuptools import setup, find_packages

setup(
    name="ENRGAI",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas"
    ],
    author="Behdad Ehsani",
    author_email="behdad.ehsani@enrg-ai.ca",
    description="A library to fetch and merge data from ENRG-AI APIs.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
