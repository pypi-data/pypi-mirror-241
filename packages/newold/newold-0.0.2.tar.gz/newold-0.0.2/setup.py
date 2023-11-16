import setuptools

name = "newold"
libname = name.replace("-", "_")

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

version_file = "{}/version.py".format(libname)
with open(version_file) as fi:
    vs = {}
    exec(fi.read(), vs)
    __version__ = vs["__version__"]

setuptools.setup(
    name=name,
    version=__version__,
    author="Eloy Pérez González",
    url="https://gitlab.com/Zer1t0/newold",
    description="Print only new values to stdout, or those that weren't seen in a while.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "{} = {}.__main__:main".format(name, libname),
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
