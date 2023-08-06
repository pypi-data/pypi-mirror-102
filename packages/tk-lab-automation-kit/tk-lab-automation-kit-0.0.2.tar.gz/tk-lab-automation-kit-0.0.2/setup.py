import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tk-lab-automation-kit",
    version="0.0.2",
    author="Dominik Werner",
    author_email="dominik.werner@live.com",
    description="A small library to create user interfaces for lab automation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dowerner/TkLabAutomationKit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'numpy>=1.20.2',
        'matplotlib>=3.4.1',
        'pyscreenshot>=3.0',
        'pyserial>=3.5',
        'PyVISA>=1.11.3',
        'PyVISA-py>=0.5.2'
    ]
)