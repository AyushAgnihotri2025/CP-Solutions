#User function Template for python3

def quickSort(head):
    #return head after sorting
    if not head or not head.next:
        return head
    pivot = head
    smallhead = small = Node(-1)
    largehead = large = Node(-1)
    curr = head.next
    while curr:
        if curr == pivot:
            curr = curr.next
        elif curr.data<pivot.data:
            small.next = curr
            curr = curr.next
            small = small.next
        else:
            large.next = curr
            curr = curr.next
            large = large.next
    small.next = None
    large.next = None
    small = quickSort(smallhead.next)
    pivot.next = None
    large = quickSort(largehead.next)
    temp = small
    while temp and temp.next:
        temp = temp.next
    if temp:
        temp.next =pivot
    else:
        small = pivot
    pivot.next = large
    return small
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        
def nodeID(head,dic):
    while head:
        dic[head.data].append(id(head))
        head=head.next
        


def printList(head,dic):
    while head:
        if id(head) not in dic[head.data]:
            print("Do'nt swap data, swap pointer/node")
            return
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().split()]
        
        ll=Llist()
        tail=None
        
        for nodeData in arr:
            tail=ll.insert(nodeData,tail)
            
        dic=defaultdict(list)   # dictonary to keep data and id of node
        nodeID(ll.head,dic)     # putting data and its id
        
        resHead=quickSort(ll.head)
        printList(resHead,dic)  #verifying and printing
        print()
        
    
    
# } Driver Code Ends