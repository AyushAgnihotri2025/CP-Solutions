#User function Template for python3
import math

class Solution:
    def find(self, N):
        # code here
        len_ = int(math.log(N, 2)) + 1
        n2 = N
        for i in range(len_):
            n2 = n2 ^ (1 << i)
        return abs(N - n2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.find(N))
# } Driver Code Ends