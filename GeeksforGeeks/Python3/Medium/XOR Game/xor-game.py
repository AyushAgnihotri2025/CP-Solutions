#User function Template for python3

class Solution:
    def xorCal(self, k):
        # code here
        return 2 if k==1 else k//2 if (k&(k+1))==0 else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        k = int(input())
        
        ob = Solution()
        print(ob.xorCal(k))
# } Driver Code Ends