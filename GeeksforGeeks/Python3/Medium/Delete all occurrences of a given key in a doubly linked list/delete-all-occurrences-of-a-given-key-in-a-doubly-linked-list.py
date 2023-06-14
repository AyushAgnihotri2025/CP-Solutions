#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        # code here
        # edit the linked list
        if head is None:
            return head
        elif head.next is None :
            if head.data == x:
                return None
            return head
        temp=head
        while temp is not None:
            if temp.data == x:
                if temp == head:
                    if temp.next is not None:
                        head=temp.next
                        head.prev=None
                else:
                    temp.prev.next=temp.next
                    if temp.next is not None:
                        temp.next.prev=temp.prev
            temp=temp.next
        return head


#{ 
 # Driver Code Starts.
#Contributed by : Ayush Kumar

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def push(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(-1)
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print(' ')
    
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        LL = LinkedList() # create a new linked list 'a'.
        inp = list(map(int, input().strip().split()))
        for x in inp:
            LL.push(x)
        key = int(input())
        obj = Solution()
        LL.head = obj.deleteAllOccurOfX(LL.head, key)
        LL.printList()
# } Driver Code Ends