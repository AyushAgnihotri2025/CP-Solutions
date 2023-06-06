'''
# node class:

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    def sum_at_distK(self, root, target, k):
        # Your code goes here
        self.ans = 0
        self.solve(root, target, k)
        return self.ans
        
    def solve(self, p, target, k):
        if not p:
            return (0, -1)
        if p.data == target:
            self.ans += p.data
            self.solve2(p.left, k)
            self.solve2(p.right, k)
            return (1, k)
        left = self.solve(p.left, target, k)
        if left[0] == 1:
            if left[1] > 0:
                self.ans += p.data
                self.solve2(p.right, left[1] - 1)
            return (1, left[1] - 1)
        right = self.solve(p.right, target, k)
        if right[0] == 1:
            if right[1] > 0:
                self.ans += p.data
                self.solve2(p.left, right[1] - 1)
            return (1, right[1] - 1)
        return (0, -1)

    def solve2(self, p, k):
        if not p:
            return
        if k > 0:
            self.ans += p.data
            self.solve2(p.left, k - 1)
            self.solve2(p.right, k - 1)

#{ 
 # Driver Code Starts
#driver code:
from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input()
        root=buildTree(line)
        line=input().strip().split()
        target=int(line[0])
        k=int(line[1])
        obj = Solution();
        print(obj.sum_at_distK(root,target,k))


# } Driver Code Ends