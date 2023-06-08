"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        head_list = []
        visited = {}
        counter = 0
        while head:
            head_list.append(head)
            visited[head] = counter
            counter +=1
            head = head.next
        ans = Node(0, None, None)
        ans_list = []
        for x in head_list:
            ans.val, ans.next = x.val, Node(0, None, None)
            ans_list.append(ans)
            ans = ans.next
        ans_list[-1].next = None
        ans = ans_list[0]
        for i, x in enumerate(head_list):
            if x.random:
                ans_list[i].random = ans_list[visited[x.random]]
        return ans_list[0]