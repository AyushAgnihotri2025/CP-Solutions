#User function Template for python3
import heapq

class Solution:
    def minOperations(self,a,n):
        # code here
        operations=0
        minheap=[]
        diff=0
        for i in range(0,n):
            if minheap and a[i]>minheap[0]:
                diff=a[i]-minheap[0]
                operations=operations+diff
                heapq.heappop(minheap)
                heapq.heappush(minheap,a[i])
            heapq.heappush(minheap,a[i])
        return operations

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=[int(x) for x in input().strip().split()]
        obj=Solution()
        print(obj.minOperations(a,n))


# } Driver Code Ends