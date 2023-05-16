#User function Template for python3

from collections import deque

class Solution:
    def cloneTree(self, tree):
        #code here
        newMapp = {}
        oldMapp = {}
        Q = deque([tree])

        while Q:
            ptr = Q.popleft()
            oldMapp[ptr.data] = ptr
            newMapp[ptr.data] = Node(ptr.data)

            if ptr.left:
                Q.append(ptr.left)
            
            if ptr.right:
                Q.append(ptr.right)

        for key, ptr in oldMapp.items():
            if ptr.left:
                newMapp[key].left = newMapp[ptr.left.data]
            if ptr.right:
                newMapp[key].right = newMapp[ptr.right.data]
            if ptr.random:
                newMapp[key].random = newMapp[ptr.random.data] 
        return newMapp[tree.data] 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.random=None

    def __str__(self):
        return str(self.data)

def printInord(a,b):
    if (not a and not b):
        return 1
        
    if(a and b) :
        t=(int)((a.data==b.data) and printInord(a.left,b.left) and printInord(a.right,b.right))
        
        if(a.random and b.random) :
            return int(t and a.random.data==b.random.data)
            
        if (a.random==b.random) :
            return t
            
        return 0
    #if a.random.data==b.random.data and printInord(a.left,b.left) and printInord(a.right,b.right):
        #return 1
    return 0


if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        map=dict()

        n=int(input())
        arrnode=[x for x in input().split()]

        root=None
        i=0
        while i<3*n:

            n1,n2,lr=int(arrnode[i]),int(arrnode[i+1]),arrnode[i+2]

            if n1 in map:
                parent=map[n1]
            else:
                parent = Node(n1)
                map[n1] = parent

                if not root:
                    root = parent


            child=Node(n2)
            map[n2]=child

            if lr=='R':
                parent.right=child

            elif lr=='L':
                parent.left=child

            else:
                parent.random=map[n2]


            i+=3

        ansTree=Solution().cloneTree(root)

        if ansTree==root:
            print(0)
        else:
            print(int(printInord(root,ansTree)))





# } Driver Code Ends