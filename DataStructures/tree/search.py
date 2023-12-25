# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes_rec(root, target):
    # BFS recursive
    # O(n)
    # O(n)
    if not root or not target:
        return False

    return root.val == target or tree_includes(root.left, target) or tree_includes(root.right, target)


def tree_includes_bfs(root, target):
    # BFS
    # O(n)
    # O(n)
  if not root or not target:
    return False
  stack = [root]
  while stack:
    node = stack.pop()
    if node.val == target:
      return True
    if node.left:
      stack.append(node.left)
    if node.right:
      stack.append(node.right)
  return False



from collections import deque
def tree_includes_dfs(root, target):
    # DFS
    # O(n)
    # O(n)
  if not root or not target:
    return False
  queue = deque([root])
  while queue:
    node = queue.popleft()
    if node.val == target:
      return True
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return False