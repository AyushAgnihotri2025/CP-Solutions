# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA==None or headB==None:
            return None
        a = headA
        b = headB
        while a!=b:
            a = headB if a==None else a.next
            b = headA if b==None else b.next
        return a