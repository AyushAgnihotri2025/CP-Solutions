class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        negatives = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                negatives += 1
            product *= num
        return -1 if negatives % 2 == 1 else 1