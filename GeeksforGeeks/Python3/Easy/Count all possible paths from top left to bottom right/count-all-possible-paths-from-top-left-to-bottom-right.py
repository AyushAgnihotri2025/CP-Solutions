#User function Template for python3
from math import factorial

class Solution:
	def numberOfPaths(self, m, n):
		# code here
		return (factorial(m+n-2)//(factorial(n-1)*factorial(m-1))) % (10**9+7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n = input().split()
		m=int(m)
		n=int(n)
		ob = Solution();
		print(ob.numberOfPaths(m,n))

# } Driver Code Ends