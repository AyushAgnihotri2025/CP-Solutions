class Solution:
    def trailingZeroes(self, n: int) -> int:
        co = 0
        while n > 0:
            co+= n // 5
            n //= 5
        return co