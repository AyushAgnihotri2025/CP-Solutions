#User function Template for python3

from bisect import bisect_left
from sortedcontainers import SortedList

class Solution:
    def findSurpasser(self, arr, n):
        # code here
        s = SortedList()
        res = [0]*n
        for i in range(n-1,-1,-1):
            ind = bisect_left(s,arr[i],0,len(s))
            res[i] = len(s)-ind
            s.add(arr[i])
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findSurpasser(arr, n)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends