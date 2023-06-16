#User function Template for python3

class Solution:
	def numberWithNoConsecutiveOnes(self, n):
		# Code here
		MAX = 2**n
        ans = []
        for i in range(1, MAX):
            if (i & (i>>1))==0:
                ans.append(i)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.numberWithNoConsecutiveOnes(n)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends