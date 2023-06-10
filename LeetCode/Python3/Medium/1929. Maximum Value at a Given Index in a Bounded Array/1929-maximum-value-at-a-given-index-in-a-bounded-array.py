class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n

        def check(x):
            y = max(0, x - index)
            ans = (x+y) * (x-y+1) // 2
            y = max(0, x - ((n-1) - index))
            ans += (x+y) * (x-y+1) // 2
            return (ans - x)

        l, r = 0, maxSum
        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid) <= maxSum:
                l = mid
            else:
                r = mid - 1
        return l + 1