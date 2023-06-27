#User function Template for python3

class Solution:
    def union(self, head1,head2):
        # code here
        # return head of resultant linkedlist
        s=[]
        curr=head1
        while(curr):
            s.append(curr.data)
            curr=curr.next
        curr=head2
        while(curr):
            s.append(curr.data)
            curr=curr.next
        s=list(set(s))
        s.sort()
        dummy=Node(0)
        curr=dummy
        for i in s:
            curr.next=Node(i)
            curr=curr.next
        return dummy.next




#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    for _ in range(int(input())):
        
        n1 = int(input())
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        n2 = int(input())
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        
        ob = Solution()
        printList(ob.union(ll1.head,ll2.head))
        print()

# } Driver Code Ends