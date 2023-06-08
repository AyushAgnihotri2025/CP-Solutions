# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        array = []
        currentlist = head
        while currentlist is not None:
            array.append(currentlist)
            currentlist = currentlist.next
        i = 0
        halflenth = len(array)//2
        while i < halflenth:
            temp = array[i].next
            array[i].next = array[~i]
            array[~i].next = temp
            i += 1
        array[halflenth].next = None 
        return head