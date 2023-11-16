import setuptools

name = "dnsresolv"

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version_file = "{}/version.py".format(name)
with open(version_file) as fi:
    vs = {}
    exec(fi.read(), vs)
    __version__ = vs["__version__"]


setuptools.setup(
    name=name,
    version=__version__,
    author="Eloy Perez",
    author_email="zer1t0ps@protonmail.com",
    description="Resolve domains and ips",
    url="https://gitlab.com/Zer1t0/dnsresolv.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "dnsresolv = dnsresolv.main:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
