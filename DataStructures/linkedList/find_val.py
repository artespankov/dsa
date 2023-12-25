# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_find(head, target):
    curr = head
    while curr is not None:
        if curr.val == target:
            return True
        curr = curr.next
    return False


def linked_list_find_rec(head, target):
    if head is None:
        return False
    if head.val == target:
        return True
    # return head.val == target or linked_list_find_rec(head.next, target)
    return linked_list_find_rec(head, target)


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):
  i = 0
  curr = head
  while curr is not None:
    if i == index:
      return curr.val
    curr = curr.next
    i += 1
