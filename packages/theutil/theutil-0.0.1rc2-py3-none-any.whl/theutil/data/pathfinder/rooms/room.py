from typing import Dict, List, Union
from theutil.data.a_data_object import ADataObject

from theutil.data.time_series import TimeSeries

class Room(ADataObject):
    """Represents a single room in a Pathfinder simulation.

    Args:
        name (str): The full tree name of the room
        data (Dict): Raw data dict for the room from the _rooms data file.
        
    Attributes:
        name (str): The full tree name of the room
        shortname (str): The last portion of the full tree name of the room.
        usage (TimeSeries[int]): Usage data for this door over time
    """
    
    def __init__(self, *, name: str, data: Dict):
        super().__init__()
        self.name = name
        self.shortname = self.name.split('->')[-1]
        self._data = data
        
        self.usage: TimeSeries[int] = TimeSeries(time=[], values=[])
        
        self._load()
        
    def _load(self) -> None:
        self.usage = TimeSeries(time=[_ for _ in self._data.keys()], values=[int(_) for _ in self._data.values()])