#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def countNodes(self, i):
        # Code here
        return 2**(i-1)


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        i = int(input())
        ob = Solution()
        res = ob.countNodes(i)
        print(res)
# } Driver Code Ends