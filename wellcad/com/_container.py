from collections.abc import Sequence


class Container(Sequence):
    """A generic container implementing collections.abc.Sequence.
    
    Parameters
    ----------
    getter : Callable
        A function that can be used to get items from the container by integer
        index. The function must take a single integer argument and return the
        item in the container at the specified index.
    counter : Callable
        A function that can be used to get the number of items in the
        container. The function signature takes no arguments and returns an
        integer.
    """
    
    def __init__(self, getter, counter):
        self.__getter = getter
        self.__counter = counter
    
    def __len__(self):
        return self.__counter()
    
    def __getitem__(self, i):
        return self.__getter(i)