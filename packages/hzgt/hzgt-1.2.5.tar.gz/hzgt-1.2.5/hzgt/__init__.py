import os
import sys

from .version._version import __version__
version = __version__

from .strop import get_midse, perr, pic, restrop
from .fileop import getdirsize, getFileSize, getUrlFileSize
from .fileop import Bit_Unit_Conversion

