from typing import Dict
from theutil.data.a_data_object import ADataObject


class Summary(ADataObject):
    """Placeholder for Simulation Summary data.

    Args:
        data (Data): data
    """
    
    def __init__(self, *, data: Dict) -> None:
        
        # TODO implement a summary API
        
        self._load()
    
    def _load(self) -> None:
        pass