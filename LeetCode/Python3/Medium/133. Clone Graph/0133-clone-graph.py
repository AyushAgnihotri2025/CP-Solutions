"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        memo = {}
        def dfs(node):
            if not node: return
            if node in memo: return memo[node]
            clone = Node(node.val, [])
            memo[node] = clone
            for neighbor in node.neighbors:
                memo[node].neighbors.append(dfs(neighbor))
            return memo[node]
        return dfs(node)
        