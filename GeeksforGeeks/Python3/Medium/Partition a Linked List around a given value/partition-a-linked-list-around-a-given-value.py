#User function Template for python3

"""

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def partition(self, head, x):
        #code here
        sh = st = lh = lt = eh = et= None
        c = head
        while c!=None:
            if c.data == x:
                if not eh:
                    eh = c
                    et = c
                else:
                    et.next = c
                    et = c
            elif c.data < x:
                if not sh:
                    sh = c
                    st = c
                else:
                    st.next = c
                    st = c
            else:
                if not lh:
                    lh = c
                    lt = c
                else:
                    lt.next = c
                    lt = c
            c = c.next
        if et:
            et.next = None
        if lt:
            lt.next = None
        if st:
            st.next = None
        cn = None
        if et:
            et.next = lh
            cn = eh
        else:
            cn = lh
        
        if st:
            st.next = cn
            return sh
        else:
            return cn

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.partition(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends