#!/usr/bin/env python3
# Copyright (C) 2015-2018  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

from io import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


def parse_requirements(name=None):
    if name:
        reqf = "requirements-%s.txt" % name
    else:
        reqf = "requirements.txt"

    requirements = []
    if not path.exists(reqf):
        return requirements

    with open(reqf) as f:
        for line in f.readlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            requirements.append(line)
    return requirements


setup(
    name="swh.loader.core",
    description="Software Heritage Base Loader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    author="Software Heritage developers",
    author_email="swh-devel@inria.fr",
    url="https://forge.softwareheritage.org/diffusion/DLDBASE",
    packages=find_packages(),  # packages's modules
    scripts=[],  # scripts to package
    install_requires=parse_requirements() + parse_requirements("swh"),
    setup_requires=["setuptools-scm"],
    use_scm_version=True,
    extras_require={"testing": parse_requirements("test")},
    include_package_data=True,
    entry_points="""
        [swh.cli.subcommands]
        loader=swh.loader.cli
        nar=swh.loader.core.nar
        [swh.workers]
        loader.content=swh.loader.core:register_content
        loader.directory=swh.loader.core:register_directory
        loader.arch=swh.loader.package.arch:register
        loader.archive=swh.loader.package.archive:register
        loader.aur=swh.loader.package.aur:register
        loader.conda=swh.loader.package.conda:register
        loader.cpan=swh.loader.package.cpan:register
        loader.cran=swh.loader.package.cran:register
        loader.crates=swh.loader.package.crates:register
        loader.debian=swh.loader.package.debian:register
        loader.deposit=swh.loader.package.deposit:register
        loader.golang=swh.loader.package.golang:register
        loader.hackage=swh.loader.package.hackage:register
        loader.hex=swh.loader.package.hex:register
        loader.nixguix=swh.loader.package.nixguix:register
        loader.npm=swh.loader.package.npm:register
        loader.opam=swh.loader.package.opam:register
        loader.pubdev=swh.loader.package.pubdev:register
        loader.puppet=swh.loader.package.puppet:register
        loader.pypi=swh.loader.package.pypi:register
        loader.maven=swh.loader.package.maven:register
        loader.rubygems=swh.loader.package.rubygems:register
        loader.rpm=swh.loader.package.rpm:register
        loader.bioconductor=swh.loader.package.bioconductor:register
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ],
    project_urls={
        "Bug Reports": "https://forge.softwareheritage.org/maniphest",
        "Funding": "https://www.softwareheritage.org/donate",
        "Source": "https://forge.softwareheritage.org/source/swh-loader-core",
        "Documentation": "https://docs.softwareheritage.org/devel/swh-loader-core/",
    },
)
