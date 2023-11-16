"""The ``models`` package provides a generic :py:class:`theutil.models.Model` class to represent simulation files, and also contains extending classes that are specific to each supported simulator.

----

"""
from theutil.models.model import Model
from theutil.models.pathfinder import PathfinderModel
from theutil.models.ventus import VentusModel
from theutil.models.fds import FDSModel

__all__ = ["Model", "PathfinderModel", "FDSModel", "VentusModel"]