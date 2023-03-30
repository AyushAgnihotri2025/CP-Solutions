# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Check if at least one of the list is empty
        if not list1 and not list2:
            return ListNode(0).next
        if not list1:
            return list2
        if not list2:
            return list1

        result = []
        
        # Compare the values of the two lists starting from the head nodes
        # and add the smaller value to the result list
        while list1 and list2:
            if list1.val <= list2.val:
                result.append(list1)
                list1 = list1.next
            else:
                result.append(list2)
                list2 = list2.next

        # Add remaining nodes from non-empty list to the result list
        while list1:
            result.append(list1)
            list1 = list1.next
        while list2:
            result.append(list2)
            list2 = list2.next

        # Create a new linked list using the nodes in the result list
        for i in range(len(result)-1):
            result[i].next = result[i+1]
        result[-1].next = None
        
        return result[0]