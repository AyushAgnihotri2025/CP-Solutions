# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self, head: ListNode):
        self.head = head
        self.length = 0
        node = head
        while node:
            self.length += 1
            node = node.next

    def getRandom(self) -> int:
        index = random.randint(0, self.length - 1)
        node = self.head
        for i in range(index):
            node = node.next
        return node.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()