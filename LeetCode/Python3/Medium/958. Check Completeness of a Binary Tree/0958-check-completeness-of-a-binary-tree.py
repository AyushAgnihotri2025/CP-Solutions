from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        is_last_level = False

        while queue:
            node = queue.popleft()

            # If we've already seen a node with a missing child,
            # then all subsequent nodes must also be leaf nodes.
            if (node.left is None and node.right is not None) or is_last_level and (node.left is not None or node.right is not None):
                return False

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            # If we've reached a level where a node is missing a child,
            # then all subsequent nodes must also be missing children.
            if node.left is None or node.right is None:
                is_last_level = True

        return True