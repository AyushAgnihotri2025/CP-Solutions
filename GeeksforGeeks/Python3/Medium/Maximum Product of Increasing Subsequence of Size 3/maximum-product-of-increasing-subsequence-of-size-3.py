#User function Template for python3

import sys
import bisect

class Solution:
    def countArray (self, arr, n) : 
        # Complete the function
        g = [-1] * n
        maxi = arr[-1]
        for i in range(n - 2, -1, -1):
            g[i] = max(maxi, arr[i])
            maxi = g[i]
        s = [arr[0]]
        re = -sys.maxsize
        l = [-1]
        for i in range(1, n - 1):
            x = bisect.bisect_left(s, arr[i])
            if x != 0 and g[i] > arr[i] and arr[i] * g[i] * s[x - 1] > re:
                re = arr[i] * g[i] * s[x - 1]
                l = [s[x - 1], arr[i], g[i]]
            bisect.insort(s, arr[i])
        return l

#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = Solution().countArray(arr, n)
    if(ans[0] == -1):
        print("Not Present")
    else:
        print(*ans)
# } Driver Code Ends