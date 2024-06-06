from typing import Any

class Dequeue:
    """
    Dequeue - double-ended queue, ordered collection of items similar to both Stack & Queue by proprties,
    besides doesn't imply FIFO or FILO but items can be added or removed from both ends

    Add/remove from front O(1)
    Add/remove from rear is O(n)
    Q: where the front & rear assigned in certain implementation
    """

    def __init__(self):
        self.items = []

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_rear(self):
        if self.items:
            return self.items.pop(0)
        raise Exception("Dequeue is empty")

    def add_front(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.items:
            return self.items.pop()
        raise Exception("Dequeue is empty")

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

