class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda total, el: total ^ el, nums)