#User function Template for python3

class Solution:
    def isPerfectNumber(self, N):
        # code here 
        return +(N in (6, 28, 496, 8128, 33550336, 8589869056, 137438691328))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends