from typing import Any


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, elem: Any):
        self.items.insert(0, elem)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
