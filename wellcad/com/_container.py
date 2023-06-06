from collections.abc import Sequence


class Container(Sequence):
    def __init__(self, getter, counter):
        self.__getter = getter
        self.__counter = counter
    
    def __len__(self):
        return self.__counter()
    
    def __getitem__(self, i):
        return self.__getter(i)