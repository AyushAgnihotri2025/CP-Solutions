#User function Template for python3

import math

class Solution:
    def facDigits(self, N):
        #code here
        if N==0:
            return 1
        else:
            x = ((N * math.log10(N / math.e) + math.log10(2 * math.pi * N) /2.0))
        return int(x)+1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.facDigits(N))
# } Driver Code Ends