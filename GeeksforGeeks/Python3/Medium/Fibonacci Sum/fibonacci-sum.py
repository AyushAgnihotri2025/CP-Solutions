#User function Template for python3

class Solution:
    def fibSum (self,N):
        # code here
        if N <= 0:
            return 0
        if N == 1:
            return 1
        a, b = 0, 1
        s = 1
        for _ in range(2, N + 1):
            a, b = b, (a + b) % 1000000007
            s = (s+b) % 1000000007
        return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.fibSum(N))
# } Driver Code Ends