#User function Template for python3

'''
class MinHeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None
'''


#Function to return the decoded string.
def decodeHuffmanData(root, binaryString):
    #your code here
    length = len(binaryString)
    head = root
    i = 0
    stringAns = ""

    while i < length:
      char = binaryString[i]
      if char == '0' and root.data == '$':
        root = root.left
        i += 1
      elif char == '1' and root.data == '$':
        root = root.right
        i += 1
      elif root.left is None and root.right is None:
        stringAns += root.data
        root = head

    stringAns += root.data
    return stringAns


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import heapq
minheap = []
heapq.heapify(minheap)
cnt=0
codes = {}
freq = {}

class MinHeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

def printCodes(root, strr):
    if root==None:
        return
    if root.data is not '$':
        print(str(root.data)+": "+strr)
    printCodes(root.left, strr+"0")
    printCodes(root.right, strr+"1")

def storeCodes(root, strr):
    if root==None:
        return
    if root.data is not '$':
        codes[root.data]=strr
    storeCodes(root.left, strr+"0")
    storeCodes(root.right, strr+"1")

def huffmanCodes(s):
    global cnt
    for v in freq:
        heapq.heappush(minheap, (freq[v], freq[v]+cnt, MinHeapNode(v, freq[v])))
        cnt+=1
    while(len(minheap) is not 1):
        left = minheap[0][2]
        heapq.heappop(minheap)
        right = minheap[0][2]
        heapq.heappop(minheap)
        top = MinHeapNode('$', left.freq+right.freq)
        top.left = left
        top.right = right
        heapq.heappush(minheap, (top.freq, top.freq+cnt, top))
        cnt+=1
    storeCodes(minheap[0][2], "")


def calcFreq(strr, n):
    for i in range(n):
        if strr[i] not in freq:
            freq[strr[i]]=1
        else:
            freq[strr[i]]+=1


if __name__ == "__main__":
    t = int(input())
    while(t>0):
        strr = input()
        encodedString = ""
        decodedString = ""
        calcFreq(strr, len(strr))
        #print(freq)
        huffmanCodes(len(strr))
        #print(codes)
        for i in strr:
            encodedString += codes[i]

        decodedString = decodeHuffmanData(minheap[0][2], encodedString)
        print(decodedString)
        t=t-1


# } Driver Code Ends