# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = dict()
        def bfs(curr = root, level = 0):
            nonlocal ans
            if curr:
                bfs(curr.left, level + 1)
                bfs(curr.right, level + 1)
                if level not in ans.keys():
                    ans[level] = [curr.val]
                else:
                    ans[level].append(curr.val)
            return
        bfs()
        answer = []
        for i in reversed(sorted(ans.keys())):
            answer.append(ans[i])
        return answer