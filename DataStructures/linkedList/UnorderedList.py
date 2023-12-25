
from typing import Any


class ListNode:
    def __init__(self, value: Any, next: 'ListNode' = None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, new_value: Any):
        self.value = new_value

    def set_next(self, new_next: 'ListNode'):
        self.next = new_next


class UnorderedList:
    """
    Unordered linked list
    """

    def __init__(self):
        self.head = None

    def add(self, value: int):
        new_node = ListNode(value)
        new_node.set_next(self.head)
        self.head = new_node

    def remove(self, item: Any):
        pass

    def search(self, item) -> bool:
        curr: ListNode = self.head
        while curr:
            if curr.get_value() == item:
                return True
            curr = curr.get_next()
        return False


    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        count = 0
        curr: ListNode = self.head
        while curr:
            count += 1
            curr = curr.get_next()
        return count

    def append(self, item: Any):
        pass

    def insert(self, pos: int, item: Any):
        pass

    def index(self, item: Any) -> int:
        pass

    def pop(self, pos: int = None) -> Any:
        pass



