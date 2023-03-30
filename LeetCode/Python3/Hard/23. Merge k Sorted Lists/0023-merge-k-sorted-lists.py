# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a min-heap of size k
        heap = []
        for i, lst in enumerate(lists):
            if lst is not None:
                heapq.heappush(heap, (lst.val, i, lst))
        
        # Merge the linked lists using the heap
        dummy = ListNode(-1)
        curr = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next