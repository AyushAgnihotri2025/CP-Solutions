# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = defaultdict(list)
        def helper(left, right):
            if left > right:
                return [None]
            if (left, right) in dp:
                return dp[(left, right)]
            for i in range(left, right+1):
                lefts = helper(left, i-1)
                rights = helper(i+1, right)
                for l in lefts:
                    for r in rights:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        dp[(left, right)].append(root)
            return dp[(left, right)]
        return helper(1, n)