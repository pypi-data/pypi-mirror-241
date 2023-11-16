"""The theutil package is an API for processing the output data of many common Life Safety simulators.
It is specifically inteneded for use in the Scripting Engine of the `Thunderhead Results Viewer <https://support.thunderheadeng.com/docs/pyrosim/2022-3/results-user-manual/>`_,
however is designed for use outside of that environment if desired.

Attributes:
    log(Optional[logging.Logger]): A preconfigured logger that writes output to the script log file.
"""
import sys, os

from theutil.main import *
from theutil.data.data_file import DataFile
from theutil.logging import get_theutil_logger, _initialize_logger

log: Optional[logging.Logger] = None
if 'sphinx' not in sys.argv[0]:
    _initialize_logger()
    log = get_theutil_logger(sys.argv[0])   
    
__all__ = ["get_models", "get_pathfinder_models", "get_pyrosim_models", "get_ventus_models", "get_theutil_logger"]

VERSION = "0.0.1RC9"