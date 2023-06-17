#User function Template for python3

class Solution:
	def DivCountSum(self, n):
		# Code here
		ans=0
        for i in range(1,n+1):
            ans+=(n//i)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.DivCountSum(n)
		print(ans)

# } Driver Code Ends