# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def level_order(root: TreeNode | None) -> Iterable[Sequence[TreeNode]]:            
            level = () if root is None else (root,)
            while level:
                yield level
                level = tuple(child for node in level for child in (node.left, node.right) if child)

        return [[node.val for node in level] for level in level_order(root)]