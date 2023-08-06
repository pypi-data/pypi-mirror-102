from setuptools import setup

import versioneer

dev_requires = ["pytest", "black", "flake8", "pre-commit"]
extras = {
    "dev": dev_requires,
}

setup(
    name="gami",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Gami Authors",
    author_email="wesr000@gmail.com",
    description="Scaffold your data and produce random values.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/WesRoach/gami",
    license="MIT",
    packages=["gami"],
    install_requires=[],
    extras_require=extras,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.7",
)
