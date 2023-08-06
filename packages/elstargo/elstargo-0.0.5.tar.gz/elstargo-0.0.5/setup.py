import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elstargo", # Replace with your own username
    version="0.0.5",
    author="Elstargo",
    author_email="tagam2707@gmail.com",
    description="FOR THE GREATER GOOD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Elstargo00/elstargo_package.git",
    packages=setuptools.find_packages(include=['elstargo','datamanagement']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_required = [],
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest==4.4.1'],
    test_suite='tests',
)
