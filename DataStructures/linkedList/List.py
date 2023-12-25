from typing import Any

class UnorderedList:

    def __int__(self):
        self.items = []

    def add(self, item: Any):
        pass

    def remove(self, item: Any):
        pass

    def search(self, item) -> bool:
        pass

    def is_empty(self) -> bool:
        pass

    def size(self) -> int:
        pass

    def append(self, item: Any):
        pass

    def insert(self, pos: int, item: Any):
        pass

    def index(self, item: Any) -> int:
        pass

    def pop(self, pos: int = None) -> Any:
        pass


class Node:
    def __init__(self, val: int = 0, next: 'Node' = None):
        self.next = next
        self.val = val

    def get_value(self):
        return self.val

    def get_next(self):
        return self.next

    def set_value(self, new_val: int):
        self.val = new_val

    def set_next(self, new_next: 'Node'):
        self.next = new_next
