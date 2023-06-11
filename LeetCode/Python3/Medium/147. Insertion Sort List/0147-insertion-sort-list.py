# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        res=[]
        while(temp):
            res.append(temp.val)
            temp=temp.next
        res.sort()
        new=head
        i=0
        while new:
            new.val = res[i]  
            i += 1
            new = new.next
        return head