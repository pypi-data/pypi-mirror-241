import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qiskit_quantier",
    version="0.9.0",
    description="QUANTier version of provider for Qiskit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["qiskit_quantier"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "qiskit",
        "qiskit-aer",
        "python-dotenv",
        "mysql-connector-python",
        "httpx"
    ],
    python_requires='>=3.8',
    include_package_data=True,
)
