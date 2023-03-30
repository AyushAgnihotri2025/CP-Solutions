class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
                count += zeros
            else:
                zeros = 0
        return count