from typing import Iterable, List, Union
from theutil.data.collection import ADataCollection
from theutil.data.pathfinder.groups.group import Group


class GroupCollection(ADataCollection):
    """Collection of Group objects that provides array-like interface to make accessing Group data a little easier.
    
    Example:
        Elements in the Collection can be accessed in the following ways:
            - GroupCollection[str] => Gets the first Group object whose name matches the provided string.
            - GroupCollection[int] => Returns the Group object at the index specified by int.

    Arguments:
        *groups (Union[Iterable, List]): Group objects to put in the collection
    """
    
    def __init__(self, *groups: Union[Iterable, List]):
        super().__init__(*groups)
        
    def __getitem__(self,  key: Union[int, str]) -> Union[Group, List[Group]]:
        if type(key) == int:
            return self._elements[key]
        else:
            return next(group for group in self._elements if (group.name == key))