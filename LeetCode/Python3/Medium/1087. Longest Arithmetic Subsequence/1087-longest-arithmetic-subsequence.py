class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        d = [collections.defaultdict(int) for _ in nums]
        res = 1
        for i in range(0,len(nums)):
            for j in range(i):
                v = nums[i]-nums[j]
                d[i][v]=max(d[j][v]+1,d[i][v])
                res = max(d[i][v],res)
        return res+1