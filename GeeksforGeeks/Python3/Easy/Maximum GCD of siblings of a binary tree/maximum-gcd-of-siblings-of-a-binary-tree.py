#User function Template for python3

from math import gcd

class Solution:
    def maxBinTreeGCD(self, arr, N):
        # code here 
        if len(arr) <= 1:
            return 0
        arr.sort()
        a = arr[0]
        ans = 0
        for i in range(1, len(arr)):
            b = arr[i]
            if b[0] == a[0]:
                ans = max(ans, gcd(a[1], b[1]))
            a = b
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from math import gcd
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=[]
        
        for i in range(N-1):
            u,v=map(int,input().split())
            arr.append([u,v])
        
        ob = Solution()
        print(ob.maxBinTreeGCD(arr,N))
# } Driver Code Ends