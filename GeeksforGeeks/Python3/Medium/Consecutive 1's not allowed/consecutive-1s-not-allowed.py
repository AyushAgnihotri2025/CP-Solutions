#User function Template for python3
class Solution:

	def countStrings(self,n):
    	# code here
    	mod=10**9+7
        l=[0 for i in range(n+1)]
        l[0]=1
        l[1]=2
        for i in range(2,n+1):
            l[i]=l[i-1]+l[i-2]
        return l[-1]%mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
# } Driver Code Ends