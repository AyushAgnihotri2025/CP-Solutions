#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

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
    

# } Driver Code Ends
#User function Template for python3

class Solution:
    # Your task is to complete this function
    # function should print the node whose subtrees has exactly k leaves 
    # if no such leaves is present print -1    
    def btWithKleaves(self, root, k):
        # Code here
        res = []
        def t(rt):
            if rt is None:
                return 0
            if rt.left is None and rt.right is None:
                return 1
            l = t(rt.left)
            r = t(rt.right)
            if l + r == k:
                res.append(rt.data)
            return (l + r)
        t(root)
        return res if res else [-1]

#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        k=int(input())
        s=input()
        root=buildTree(s)
        nodes = Solution().btWithKleaves(root, k)
        for node in nodes:
            print(node,end=' ')
        print()


# } Driver Code Ends