from distutils.core import setup

from pkg_resources import resource_filename
from setuptools import setup
import os


def _load_famegui_version():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    init_filepath = os.path.join(this_dir, "famegui", "__init__.py")

    with open(init_filepath) as f:
        for line in f.readlines():
            if line.startswith("__version__"):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
    raise RuntimeError("Unable to find version string in {}".format(init_filepath))


def _readme():
    with open("README.md") as f:
        return f.read()


VERSION = _load_famegui_version()

setup(
    name="famegui",
    packages=[
        "famegui",
        "famegui.config",
        "famegui.dialogs",
        "famegui.generated",
        "famegui.models",
        "famegui.database",
        "famegui.ui",
    ],
    version=VERSION,
    keywords=["FAME", "agent-based modelling"],
    license="Apache License 2.0",
    description="Graphical user interface to the FAME modelling framework",
    long_description=_readme(),
    long_description_content_type="text/markdown",
    author="Aurélien Regat-Barrel, Simon Wischnevetski",
    author_email="fame@dlr.de",
    url="https://gitlab.com/fame-framework/FAME-Gui",
    download_url="https://gitlab.com/fame-framework/FAME-Gui/-/archive/v{}/FAME-Gui-v{}.tar.gz".format(
        VERSION, VERSION
    ),
    install_requires=[
        "coloredlogs",
        "fameio>=1.6.3",
        "python-igraph",
        "pyyaml",
        "ipython",
        "PySide2",
        "SQLAlchemy>=1.4.44",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={
        "console_scripts": [
            "famegui=famegui.app:run",
        ],
    },
    package_data={
        "famegui": ["data/*", "database/database.sqlite3", "*sqlite3"],
    },
    DB_PATH=resource_filename("famegui", "database/database.sqlite3"),
)
