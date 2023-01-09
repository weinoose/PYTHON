from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Science/Research",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "Operating System :: Microsoft :: Windows :: Windows 8.1",
    "Operating System :: Microsoft :: Windows :: Windows 8",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name = "pass",
    version = "1.0.0",
    description = "pass.",
    long_description = open("README.txt").read() + "\n\n" + open("CHANGELOG.txt").read(),
    url = "https://github.com/WEINOOSE",
    author = "Emir Yarkın Yaman",
    author_email = "emiryarkinyaman@gmail.com",
    license = "MIT",
    classifiers = classifiers,
    keywords = "PYTHON ML DL DS AI",
    packages = find_packages(),
    install_requires=[
        'opencv-python',
        'tensorflow',
        'numpy',
        'matplotlib',
    ]
)