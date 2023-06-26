#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def XOR(self, n, m):
        # Code here
        return n^m

    def check(self, a, b):
        # Code here
        return 1 if (1<<(a-1))&b else 0

    def setBit(self, c, d):
        # Code here
        return d|(1<<c)


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        a, b = list(map(int, input().split()))
        c, d = list(map(int, input().split()))
        ob = Solution()
        ans1 = ob.XOR(n, m)
        ans2 = ob.check(a, b)
        ans3 = ob.setBit(c, d)
        print(ans1, ans2, ans3)
# } Driver Code Ends