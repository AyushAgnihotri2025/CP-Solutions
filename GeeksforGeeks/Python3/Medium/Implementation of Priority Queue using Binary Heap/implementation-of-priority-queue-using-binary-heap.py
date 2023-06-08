#{ 
 # Driver Code Starts
#Initial Template for Python 3
H = [0] * 10009
s = -1

def parent(i):
    return (i - 1) // 2
    
def leftChild(i):
    return 2 * i + 1
    
def rightChild(i):
    return 2 * i + 2
    
def shiftUp(i):
    while i > 0 and H[parent(i)] < H[i]:
        H[parent(i)], H[i] = H[i], H[parent(i)]
        i = parent(i)
        
def shiftDown(i):
    maxIndex = i
    l = leftChild(i)
    if l <= s and H[l] > H[maxIndex]:
        maxIndex = l
    r = rightChild(i)
    if r <= s and H[r] > H[maxIndex]:
        maxIndex = r
    if (i != maxIndex):
        H[i], H[maxIndex] = H[maxIndex], H[i]
        shiftDown(maxIndex)

def insert(p):
    global s
    s += 1
    H[s] = p
    shiftUp(s)
    

# } Driver Code Ends
#User function Template for python3

# 1. parent(i): Function to return the parent node of node i
# 2. leftChild(i): Function to return index of the left child of node i
# 3. rightChild(i): Function to return index of the right child of node i
# 4. shiftUp(int i): Function to shift up the node in order to maintain the
# heap property
# 5. shiftDown(int i): Function to shift down the node in order to maintain the
# heap property.
# int s=-1, current index value of the array H[].


class Solution:
    def extractMax(self):
        # Code here
        global s
        res = H[0]
        H[0] = H[s]
        s -= 1
        shiftDown(0)
        return res

#{ 
 # Driver Code Starts.

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        a = list(map(int, input().split()))
        for val in a:
            insert(val)
        ob = Solution()
        print('Node with maximum priority :', ob.extractMax())
        print('Priority queue after extracting maximum : ', end = '')
        for i in range(s + 1):
            print(H[i], end = ' ')
        print()
# } Driver Code Ends