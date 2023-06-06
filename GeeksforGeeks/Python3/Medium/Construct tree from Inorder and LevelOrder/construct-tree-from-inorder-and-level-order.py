#User function Template for python3

'''
class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
'''

def buildTree(level, ino):
    # code here
    # return root of tree
    return solve(level,0) 

def solve(lev,i):
    root=None
    if i<len(lev):
        root=Node(lev[i])
        root.left=solve(lev,2*i+1)
        root.right=solve(lev,2*i+2)
    return root
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def preOrd(root):
    if not root:
        return
    print(root.data,end=' ')
    preOrd(root.left)
    preOrd(root.right)

if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())

        InOrd=[int(x) for x in input().split()]
        LvlOrd=[int(x) for x in input().split()]

        root=buildTree(LvlOrd,InOrd)

        preOrd(root)
        print()


# } Driver Code Ends