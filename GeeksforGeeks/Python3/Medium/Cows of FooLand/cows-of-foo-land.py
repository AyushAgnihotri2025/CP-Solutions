#User function Template for python3

class Solution:
	def multiple(self, a, b, m):
        ans = [[0, 0], [0, 0]]
        ans[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % m
        ans[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % m
        ans[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % m
        ans[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % m
        return ans
    def binpow(self, a, n, m):
        ans = [[1, 0], [0, 1]]
        while n > 0:
            if n & 1:
                ans = self.multiple(ans, a, m)
            a = self.multiple(a, a, m)
            n >>= 1
        return ans
    def TotalAnimal(self, N):
        # Code here
        M = int(1e9+7)
        a = [[1, 1], [1, 0]]
        a = self.binpow(a, N, M)
        return a[0][0]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.TotalAnimal(N)
		print(ans)
# } Driver Code Ends