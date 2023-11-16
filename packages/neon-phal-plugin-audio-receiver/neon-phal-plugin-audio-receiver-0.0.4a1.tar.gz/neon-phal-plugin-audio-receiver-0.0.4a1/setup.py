#!/usr/bin/env python3
import os
from setuptools import setup

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def get_version():
    """Find the version of the package"""
    version = None
    version_file = os.path.join(BASEDIR, "neon_phal_plugin_audio_receiver", "version.py")
    major, minor, build, alpha = (None, None, None, None)
    with open(version_file) as f:
        for line in f:
            if "VERSION_MAJOR" in line:
                major = line.split("=")[1].strip()
            elif "VERSION_MINOR" in line:
                minor = line.split("=")[1].strip()
            elif "VERSION_BUILD" in line:
                build = line.split("=")[1].strip()
            elif "VERSION_ALPHA" in line:
                alpha = line.split("=")[1].strip()

            if (major and minor and build and alpha) or "# END_VERSION_BLOCK" in line:
                break
    version = f"{major}.{minor}.{build}"
    if alpha and int(alpha) > 0:
        version += f"a{alpha}"
    return version


def package_files(directory):
    paths = []
    for path, directories, filenames in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


def required(requirements_file):
    """Read requirements file and remove comments and empty lines."""
    with open(os.path.join(BASEDIR, requirements_file), "r") as f:
        requirements = f.read().splitlines()
        if "MYCROFT_LOOSE_REQUIREMENTS" in os.environ:
            print("USING LOOSE REQUIREMENTS!")
            requirements = [r.replace("==", ">=").replace("~=", ">=") for r in requirements]
        return [pkg for pkg in requirements if pkg.strip() and not pkg.startswith("#")]


def get_description():
    with open(os.path.join(BASEDIR, "README.md"), "r") as f:
        long_description = f.read()
    return long_description


PLUGIN_ENTRY_POINT = "neon-phal-plugin-audio-receiver=neon_phal_plugin_audio_receiver:AudioReceiver"
setup(
    name="neon-phal-plugin-audio-receiver",
    version=get_version(),
    description="A plugin for OVOS/NEON that allows the user to control the audio receiver options by voice command.",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/NeonGeckoCom/neon-phal-plugin-audio-receiver",
    author="mikejgray",
    author_email="mike@graywind.org",
    license='BSD-3',
    packages=["neon_phal_plugin_audio_receiver"],
    package_data={"": package_files("neon_phal_plugin_audio_receiver")},
    install_requires=required("requirements.txt"),
    zip_safe=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    entry_points={"ovos.plugin.phal.admin": PLUGIN_ENTRY_POINT},
)
