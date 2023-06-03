"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        q = deque([root])
        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                if i < level_size - 1:
                    node.next = q[0]
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return root