

class Array:
    """
    Dynamic array implementation
    Doubles each time when the internal (static) array is full
    """
    arr: list = []  # internal static array
    length: int  # length that user thinks aray is
    capacity: int  # actual size of the array

    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError(f"Illegal capacity {capacity}")
        self.capacity = capacity

    def __len__(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return len(self) == 0

    def __getitem__(self, item):
        return self.arr[item]

    def __setitem__(self, key, value):
        self.arr[key] = value

