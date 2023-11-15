from typing import Generic, List, TypeVar

T = TypeVar("T") 

class TimeSeries(Generic[T]):
    """Used to store Time Series based data about a Simulation
    
    Args:
        time (List[float]): Timesteps at which the data was written.
        values (List): A list of data corresponding to the Timesteps
            
    Attributes:
        time (List[float]): Timesteps at which the data was written.
        values (List[T]): A list of data corresponding to the Timesteps
    """
    
    def __init__(self, *, time: List[float], values: List[T]) -> None:
        self.time: List[float] = time
        self.values: List[T] = values