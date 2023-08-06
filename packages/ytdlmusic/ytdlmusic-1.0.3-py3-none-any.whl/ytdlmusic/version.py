"""
version utils scripts
"""


import sys
from shutil import which
import pkg_resources
from ytdlmusic.const import NOT_INSTALLED


def python_version():
    """
    obtain the Python version
    """
    try:
        pythonversion = "".join(sys.version.splitlines())
    except Exception:
        pythonversion = NOT_INSTALLED
    return pythonversion


def binary_path(binary):
    """
    obtain 'binary' path
    """
    if which(binary) is None:
        path = NOT_INSTALLED
    else:
        path = which(binary)
    return path


def pip_package_version(package):
    """
    obtain pip 'package' version
    NOT_INSTALLED in no package found
    """
    try:
        version = pkg_resources.get_distribution(package).version
    except Exception:
        version = NOT_INSTALLED
    return version


def pip_package_version_of_double(package1, package2):
    """
    obtain package version of package1 if exists, package2 otherwise
    NOT_INSTALLED in no packages found
    """
    try:
        version = pkg_resources.get_distribution(package1).version
    except Exception:
        try:
            version = pkg_resources.get_distribution(package2).version
        except Exception:
            version = NOT_INSTALLED

    return version
