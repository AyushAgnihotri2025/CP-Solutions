# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # First, find the length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        # If k is larger than the length of the linked list, return the head
        if k > length:
            return head
        # Find the kth node from the beginning of the linked list
        curr = head
        for i in range(1, k):
            curr = curr.next
        kth_from_beginning = curr
        # Find the kth node from the end of the linked list
        curr = head
        for i in range(1, length-k+1):
            curr = curr.next
        kth_from_end = curr
        # Swap the values of the kth node from the beginning and the kth node from the end
        kth_from_beginning.val, kth_from_end.val = kth_from_end.val, kth_from_beginning.val
        
        return head