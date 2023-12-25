# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum_bfs_rec(root):
  # breadth first recursive
  # O(n)
  # O(n)
  if not root:
    return 0
  return root.val + tree_sum(root.left) + tree_sum(root.right)


def tree_sum_bfs(root):
  # breadth first
  # O(n)
  # O(n)
  if not root:
    return 0
  ans = 0
  stack = [root]
  while stack:
    node = stack.pop()
    ans += node.val
    if node.left:
      stack.append(node.left)
    if node.right:
      stack.append(node.right)
  return ans


from collections import deque
def tree_sum_dfs(root):
  # depth first
  # O(n)
  # O(n)
  if not root:
    return 0
  ans = 0
  queue = deque([root])
  while queue:
    node = queue.popleft()
    ans += node.val
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return ans
