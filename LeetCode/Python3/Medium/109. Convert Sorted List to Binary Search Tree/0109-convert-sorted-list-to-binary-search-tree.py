# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)
        
        # Find the middle element of the linked list.
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Create a new node with the value of the middle element.
        root = TreeNode(slow.next.val)
        
        # Split the linked list into two halves.
        left_half = head
        right_half = slow.next.next
        slow.next = None
        
        # Recursively construct the left and right subtrees.
        root.left = self.sortedListToBST(left_half)
        root.right = self.sortedListToBST(right_half)
        
        return root