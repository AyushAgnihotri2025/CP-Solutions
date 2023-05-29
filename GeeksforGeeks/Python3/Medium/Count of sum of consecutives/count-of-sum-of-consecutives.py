# User function Template for python3

import math

class Solution:
    def getCount(self, N):
        # code here 
        ans = 0
        maxN = math.ceil((math.sqrt(8*N+1)-1)/2)
        for n in range(2,maxN+1):
            a = N/n - (n-1)/2
            if a == round(a):
                ans += 1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.getCount(N))
# } Driver Code Ends