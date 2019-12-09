from my_pkg.my_pkg import *

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
