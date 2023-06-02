#User function Template for python3

from collections import defaultdict

class Solution:
    def findgroups(self, arr, n):
        # code here
        d = defaultdict(int)
        for a in arr:
            d[a % 3] += 1
        ans = d[1] * d[2] + d[0] * (d[0] - 1) // 2
        ans += d[0] * d[1] * d[2]
        ans += d[0] * (d[0] - 1) * (d[0] - 2) // 6
        ans += d[1] * (d[1] - 1) * (d[1] - 2) // 6 
        ans += d[2] * (d[2] - 1) * (d[2] - 2) // 6 
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findgroups(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends