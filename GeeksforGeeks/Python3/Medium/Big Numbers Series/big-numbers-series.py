#User function Template for python3

class Solution:
	def NthTerm(self, n):
		# Code here
		mod = 10**9+7
        if n == 0:
            return 0
        if n == 1:
            return 1
        c = 1
        f = 1
        for i in range(1, n):
            c*=f
            f+=1
        return ((n*n)%mod*c)%mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.NthTerm(n)
		print(ans)

# } Driver Code Ends