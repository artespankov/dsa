

class Node:

    def __init__(self, val: int):
        self.val = val
        self.next = None

    def get_val(self):
        return self.val

    def get_next(self):
        return self.next

    def set_val(self, val):
        self.val = val

    def set_next(self, new_next):
        self.next = new_next



