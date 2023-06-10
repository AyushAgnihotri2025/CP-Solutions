class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, n):
            if i > 2:
                dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
            else:
                dp[i] = nums[i] + dp[i - 2]
        return max(dp[-1], dp[-2])