#User function Template for python3

#Function to construct the BST from its given level order traversal.
def constructBst(arr,n):
    #Your code here
    root = None
    for i in range(n):
        root = insert(root, arr[i])
    return root
    
def insert(root, x):
    if not root:
        return Node(x)
    if root.data < x:
        root.right = insert(root.right, x)
    elif root.data > x:
        root.left = insert(root.left, x)
    return root
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

    
def preOrder(root):
    if root is None:
        return 
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)
    


def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
      
        root=constructBst(arr,sizeOfArray)
        
        preOrder(root)
        print()
       
        testcases-=1

if __name__=="__main__":
    main()
# } Driver Code Ends