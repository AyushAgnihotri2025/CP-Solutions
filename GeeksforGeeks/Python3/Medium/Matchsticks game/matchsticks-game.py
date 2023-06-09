#User function Template for python3

class Solution:
    def matchGame(self, N):
         # code here
         ans = N%5
         if ans == 0:
             return -1
         return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.matchGame(N))
# } Driver Code Ends