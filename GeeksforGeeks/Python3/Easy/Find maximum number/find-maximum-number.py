#User function Template for python3

class Solution:
    def findMax(self, N):
        # code here
        x=list(N)
        ans=''
        x.sort(reverse=True)
        for i in x:
            ans+=str(i)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=input()
        
        ob = Solution()
        print(ob.findMax(N))
# } Driver Code Ends