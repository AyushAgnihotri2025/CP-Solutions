
import math

class Solution:
	def Count(self, nums, k):
		# Code here
		ans = 0
        n = len(nums)
        for i in range(1, 1 << n):
            cnt = 0
            val = 1
            for j in range(n):
                if i & (1 << j):
                    cnt += 1
                    val = val * nums[j] // math.gcd(val, nums[j])
            sign = 1 if cnt % 2 else -1
            ans += sign * (k // val)
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n); k = int(k);
		nums = list(map(int, input().split()));
		ob = Solution()
		ans = ob.Count(nums, k)
		print(ans)

# } Driver Code Ends