class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        length = len(arr)
        min_val = min(arr)
        max_val = max(arr)
        diff = (max_val - min_val) / (length - 1)
        for i in range(length):
            expected = min_val + i * diff
            if expected not in arr:
                return False
        return True