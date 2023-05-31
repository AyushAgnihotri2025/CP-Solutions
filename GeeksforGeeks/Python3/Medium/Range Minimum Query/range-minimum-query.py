#User function Template for python3

import sys
seg=[0]*100000

def build(ind,arr,low,high):
    if low==high:
        seg[ind]=arr[low]
        return
    mid=low + (high-low)//2
    build(2*ind+1,arr,low,mid)
    build(2*ind+2,arr,mid+1,high)
    seg[ind]=min(seg[2*ind+1],seg[2*ind+2])
    
def constructST(arr,n):
    build(0,arr,0,n-1)
    return seg

def query(ind,low,high,l,r):
    if l>high or r<low:
        return sys.maxsize
    if l<=low and high<=r:
        return seg[ind]
    mid=low + (high-low)//2
    left=query(2*ind+1,low,mid,l,r)
    right=query(2*ind+2,mid+1,high,l,r)
    return min(left,right)

def RMQ(st, n, qs, qe):
    return query(0,0,n-1,qs,qe)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
T = int(input())

for _ in range(T):
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    segTree = constructST(A,N)
    store = [int(i) for i in input().split()]
    ans = []
    for i in range(Q):
        start,e = store[2*i],store[2*i+1]
        if(start > e):
            start,e = e,start
        ans.append(RMQ(segTree,N,start,e))
    print(*ans)
    
# } Driver Code Ends