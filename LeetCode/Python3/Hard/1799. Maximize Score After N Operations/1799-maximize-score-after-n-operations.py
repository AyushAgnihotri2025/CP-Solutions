class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def combination(count=1, bitmask=0):
            if count==size//2+1:
                return 0
            max_ = 0
            for i in range(size):
                if bitmask>>i&1:
                    continue
                newBitmask = bitmask|1<<i
                for j in range(size):
                    if newBitmask>>j&1:
                        continue
                    newBitmask = bitmask|1<<i|1<<j
                    if dp[newBitmask]:
                        max_ = max(max_, table[i][j]*count+dp[newBitmask])
                    else:
                        max_ = max(max_, table[i][j]*count+combination(count+1, newBitmask))
            dp[bitmask] = max_
            return max_
        size = len(nums)
        dp = [0]*(2**size)
        table = [[0]*size for i in range(size)]
        for i in range(size):
            for j in range(i+1, size):
                table[i][j] = table[j][i] = math.gcd(nums[i], nums[j])
        return combination()