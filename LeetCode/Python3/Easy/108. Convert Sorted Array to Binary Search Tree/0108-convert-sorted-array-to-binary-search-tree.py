# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def cv(node,vals)->TreeNode:
            if vals:
                mid=len(vals)//2
                node.val,node.left,node.right=vals[mid],cv(TreeNode(),vals[:mid]),cv(TreeNode(),vals[mid+1:])
                return node
            else:
                return None

        return cv(TreeNode(),nums)