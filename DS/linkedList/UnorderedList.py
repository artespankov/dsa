from .Node import Node


class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, val: int):
        node = Node(val)
        node.set_next(self.head)
        self.head = node


    def size(self):
        count = 0
        curr: Node = self.head
        while curr is not None:
            curr = curr.get_next()
            count += 1
        return count

    def find(self, val):
        found = False
        curr: Node = self.head
        while curr is not None and not found:
            if curr.get_val() == val:
                found = True
            else:
                curr = curr.get_next()
        return found


    def remove(self, val):
        curr: Node = self.head
        prev: Node = None
        found = False
        while curr is not None and not found:
            if curr.get_val() == val:
                found = True
                if prev is not None:
                    prev.set_next(curr.get_next())
                else:
                    self.head = self.head.get_next()
            else:
                prev = curr
                curr = curr.get_next()
        return self.head.get_val()

    def show(self):
        chain = ""
        curr: Node = self.head
        while curr is not None:
            chain = f"{chain}{curr.get_val()}->"
            curr = curr.get_next()
        print(chain)
        return chain
