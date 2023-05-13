#User function Template for python3

class Solution:
	def DistinctSum(self, nums):
		# Code here
		sums = {0}
        for x in nums:
            sums.update([s + x for s in sums])
        return sorted(sums)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.DistinctSum(nums)
		for _ in ans:
		    print(_, end = " ")
		print()

# } Driver Code Ends