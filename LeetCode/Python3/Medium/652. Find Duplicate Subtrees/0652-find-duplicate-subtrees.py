# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # Initialize the hash table and the result list
        subtrees = {}
        result = []
        
        # Helper function to serialize subtrees
        def serialize(node):
            if not node:
                return "#"
            return str(node.val) + "," + serialize(node.left) + "," + serialize(node.right)
        
        # Helper function to traverse the binary tree
        def traverse(node):
            if not node:
                return "#"
            
            # Serialize the left and right subtrees
            left = traverse(node.left)
            right = traverse(node.right)
            subtree = str(node.val) + "," + left + "," + right
            
            # Check if the subtree already exists in the hash table
            if subtree in subtrees:
                # This is a duplicate subtree
                if subtrees[subtree] == 1:
                    result.append(node)
                subtrees[subtree] += 1
            else:
                subtrees[subtree] = 1
            
            return subtree
        
        traverse(root)
        return result