#User function Template for python3

'''
heap = [0 for i in range(101)]  # our heap to be used
'''
def heapify(i):
    global curr_size, heap
    
    smallest = i
    l, r = 2*i+1, 2*i+2
    if l < curr_size and heap[smallest] > heap[l]: 
        smallest = l
    if r < curr_size and heap[smallest] > heap[r]: 
        smallest = r
    if smallest != i:
        heap[smallest], heap[i] = heap[i], heap[smallest]
        heapify(smallest)
     
        
def heapify2(i):
    global curr_size, heap
    
    parent = (i-1)//2

    while parent >= 0 and heap[parent] > heap[i]:
        heap[parent], heap[i] = heap[i], heap[parent]
        i, parent = parent, (parent-1)//2

#Function to insert a value in Heap.
def insertKey(x):
    global curr_size, heap
    heap[curr_size] = x
    curr_size += 1
    heapify2(curr_size-1)
    

#Function to delete a key at ith index.
def deleteKey(i):
    global heap, curr_size
    if i >= curr_size:
        return -1
    heap[i] = float('-inf')
    heapify2(i)
    extractMin()
    

#Function to extract minimum value in heap and then to store 
#next minimum value at first index.
def extractMin():
    global heap, curr_size
    if curr_size == 0: 
        return -1
    heap[0], heap[curr_size-1] = heap[curr_size-1], heap[0]
    r = heap[curr_size-1]
    curr_size -= 1
    heapify(0)
    return r

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

heap = []  # our heap to be used
curr_size = 0  # current size of heap

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        # initialize every globals
        curr_size = 0
        heap = [0 for i in range(n)]
        i = 0
        while i < len(a):
            if a[i] == 1:
                insertKey(a[i + 1])
                i += 1
            elif a[i] == 2:
                deleteKey(a[i + 1])
                i += 1
            else:
                print(extractMin (), end=" ")
            i += 1
        # reinitialize every globals
        # curr_size = 0
        # heap = [0 for i in range(101)]
        print()
# } Driver Code Ends