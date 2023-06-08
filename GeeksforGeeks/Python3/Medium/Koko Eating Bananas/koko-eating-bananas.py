#User function Template for python3

import math

class Solution:
    def Solve(self, N, piles, H):
        # Code here
        maxx = max(piles)
        l = 1
        r = maxx
        k = maxx
        while l <= r:
            mid = (l + r) // 2
            time = 0
            for p in piles:
                time = time + math.ceil(p / mid)
            if time <= H:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        return k

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        piles = list(map(int, input().split()))
        H = int(input())
        ob = Solution()
        print(ob.Solve(N, piles, H))
# } Driver Code Ends