# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = ListNode(data)
        if(self.head):
          current = self.head
          while(current.next):
            current = current.next
          current.next = newNode
        else:
          self.head = newNode
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = l1
        temp2 = l2
        dig1 = ''
        dig2 = ''
        while temp or temp2:
            if temp:
                dig1 += str(temp.val)
                temp = temp.next
            if temp2:
                dig2 += str(temp2.val)
                temp2 = temp2.next
        dig1 = dig1[::-1]
        dig2 = dig2[::-1]
        summ = list(str(int(dig1) + int(dig2)))
        summ.reverse()
        self.head = ListNode(int(summ[0]))
        del summ[0]
        for k in summ:
            self.insert(int(k))
        return self.head