from setuptools import setup, find_packages
import pathlib, subprocess

# inspired by https://github.com/cfengine/cf-remote/blob/master/setup.py
phaser_remote_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from th-ale README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="PHASER_tmp", # must match on pypi
    version=phaser_remote_version,
    description="A Perceptual Hashing Algorithms Evaluation and Results framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AabyWan/PHASER_tmp",
    author="Peter Aaby",
    author_email="aabywancanaaby@gmail.com",
    # Classifiers help users find your project by categorizing it.
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="research, digital forensics, development",  # Optional
    package_dir={"": "phaser"},  # Optional
    packages=find_packages(where="phaser"),  # Required
    python_requires=">=3.10, <4",
    # https://packaging.python.org/discussions/install-requires-vs-requirements/
    install_requires=["numpy", "pandas", "scipy"],  # Optional
    project_urls={  # Optional
        "Source": "https://github.com/AabyWan/PHASER_tmp/",
    },
)