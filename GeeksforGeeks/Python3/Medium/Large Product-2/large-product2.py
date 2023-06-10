#User function Template for python3

from math import log, exp, ceil

class Solution:
	def Find(self, nums):
		# Code here
		total = 0
        for a in nums:
            total += log(a)
        return ceil(exp(total/len(nums)))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.Find(nums)
		print(ans)

# } Driver Code Ends