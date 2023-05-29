#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def constructTree(pre, preLN, n):
    # code here
    if len(pre)==0:
        return None
    root=Node(pre.pop(0))
    inst=preLN.pop(0)
    if inst=="L":
        return root
    else:
        root.left=constructTree(pre,preLN,n-1)
        root.right=constructTree(pre,preLN,n-1)
    return root


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.data,end=' ')
    printInorder(root.right)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        pre = list(map(int, input().strip().split()))  # nodes
        preln=list(map(str, input().strip().split()))   # leaf or not
        # construct the tree according to given list
        root=constructTree(pre, preln, n)
        printInorder(root)
        print()
# } Driver Code Ends