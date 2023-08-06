from setuptools import setup, find_packages
import os
import subprocess
import sys
from setuptools.command.install import install


def installer(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

installer("requests")
installer("orator")
installer("termcolor")
installer("click")
installer("click-help-colors")
from DatabaseUtilities import DatabaseUtilities

class CustomInstallCommand(install):
    """Customized setuptools install command - prints a friendly greeting."""

    def run(self):
        # dbu = DatabaseUtilities()
        # dbu.setup()
        install.run(self)

# The directory containing this file
HERE = os.path.dirname(os.path.realpath(__file__))

# The text of the README file
with open(HERE + "/README.md", encoding='utf-8') as f:
    README = f.read()
with open(HERE + '/requirements.txt') as f:
    required = f.read().splitlines()
with open(HERE+'/version.txt') as f:
    version = f.read()
    setup(
        name="sego-cli",
        version=version,
        description="The command line interface for the sego framework",
        long_description_content_type="text/markdown",
        long_description=README,
        url="https://github.com/sambe-consulting/sego-cli",
        author="Sambe Consulting",
        author_email="development@sambe.co.za",
        license="Apache License 2.0",
        classifiers=[
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
        ],
        packages=find_packages(exclude=("sego_cli/tests",)),
        include_package_data=True,
        install_requires=required,
        cmdclass={
            'install': CustomInstallCommand,
        },

    )
# This call to setup() does all the work
