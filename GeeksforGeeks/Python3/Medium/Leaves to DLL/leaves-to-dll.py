#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def is_leaf(node):
    return node.right is None and node.left is None

def rec_ctd(root, aux_dict):
    if root is None:
        return
    
    if is_leaf(root):
        aux_dict.append(root)

    if root.left:
        if is_leaf(root.left):
            aux_dict.append(root.left.data)
            root.left = None
        else:
            rec_ctd(root.left, aux_dict)
    
    if root.right:
        if is_leaf(root.right):
            aux_dict.append(root.right.data)
            root.right = None
        else:
            rec_ctd(root.right,aux_dict)
            
def convertToDLL(root):
    #return the head of the DLL and remove those node from the tree as well.
    if root is None:
        return None
    aux_dict = []
    rec_ctd(root, aux_dict)
    
    first = True
    curr = None
    prev = None
    head = None
    for val in aux_dict:
        if first:
            curr = Node(val)
            curr.left = None
            curr.right = None
            head = curr
            first = False
        else:
            curr.right = Node(val)
            prev = curr
            curr = curr.right
            curr.left = prev
            curr.right = None
    return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def inOrder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated in order Traversal of the given tree.
    '''
    if root is None: # check if the root is none
        return
    inOrder(root.left) # do pre order of left child
    print(root.data, end=" ")  # print root of the given tree
    inOrder(root.right) # do pre order of right child
    
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

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root = buildTree(s)
        head = convertToDLL(root)
        inOrder(root)
        print()
        temp = head
        last = None
        while(temp != None):
            print(temp.data,end=" ")
            last = temp
            temp = temp.right
            
        print()
        temp = last;
        
        while(temp!=None):
            print(temp.data,end=" ")
            temp = temp.left
        
        print();

        

# } Driver Code Ends