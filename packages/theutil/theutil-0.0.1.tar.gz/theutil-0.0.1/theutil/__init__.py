"""`theutil </>`_ is a data processing toolset for common Life Safety simulators and a collection of utilities for displaying processed data in Thunderhead Results.
This toolset is designed for use in the Scripting Engine of the `Thunderhead Results Viewer <https://thunderheadeng.com>`_, however it can also be used in standalone Python scripts.

Attributes:
    log(Optional[logging.Logger]): A preconfigured logger that writes output to the script log file.
    VERSION(str): The version of the installed theutil package
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

VERSION: str = "0.0.1"