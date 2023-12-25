class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# def tree_min_value(root):
#   ans = root.val
#   stack = [root]
#   while stack:
#     node = stack.pop()
#     ans = min(ans, node.val)
#     if node.left:
#       stack.append(node.left)
#     if node.right:
#       stack.append(node.right)
#   return ans

# import math
# def tree_min_value(root):
#   if root is None:
#     return math.inf
#   return min(root.val, tree_min_value(root.left), tree_min_value(root.right))

from collections import deque


def tree_min_value(root):
    ans = root.val
    queue = deque([root])
    while queue:
        node = queue.popleft()
        ans = min(ans, node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ans