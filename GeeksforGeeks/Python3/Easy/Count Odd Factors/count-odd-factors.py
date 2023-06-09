#User function Template for python3


class Solution:
    def count (self, N):
        # code here
        return int(N**0.5)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Position this line where user code will be pasted.
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.count(N))

# } Driver Code Ends