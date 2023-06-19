#User function Template for python3

class Solution:
	def CommonFactor(self, n):
		# Code here
		if n<=0:
            return 0
        v=[i for i in range(0,n+1)]
        for i in range(2,n+1):
            if v[i]==i:
                for j in range(i,n+1,i):
                    v[j]*=(i-1)
                    v[j]/=i
        return int(n-v[n])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.CommonFactor(n)
		print(ans)

# } Driver Code Ends