import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="molang_chain",
    version="0.1.3",
    author="Exa",
    author_email="exa@exponent.ai",
    description="an LLM Orchestration Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["molang"],
    package_dir={'molang': '.'},
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.10',
    install_requires= required,
)
