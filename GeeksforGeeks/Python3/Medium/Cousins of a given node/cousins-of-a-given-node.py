#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printCousins(self, root, node_to_find):
        #code here
        q = [root]
        f = False
        while q:
            l = len(q)
            for i in range(l):
                p = q.pop(0)
                if p.left == node_to_find or p.right == node_to_find:
                    f = True
                else:
                    if p.left:
                        q.append(p.left)
                    if p.right:
                        q.append(p.right)
            if f:
                if q:
                    out = [n.data for n in q]
                    return out
                else:
                    return [-1]
        return [-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

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
    
def pointer(root, n):
    if root == None:
        return None
    
    if root.data == n:
        return root
        
    l= pointer(root.left, n)
    if l != None and l.data==n :
        return l
    
    r= pointer(root.right, n)
    return r
    
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n=int(input())
        s=input()
        root = buildTree(s)
        p = pointer(root, n)
        ob = Solution()
        ans = ob.printCousins(root, p)
        
        for i in range(len(ans)):
           print(ans[i], end=" ")
                
        print()
            
# } Driver Code Ends