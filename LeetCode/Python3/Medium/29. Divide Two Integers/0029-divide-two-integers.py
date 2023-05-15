class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        div = divisor
        left = dividend
        Q = 1
        ans = 0
        while left >= divisor:
            left -= div
            ans += Q
            Q+=Q
            div += div
            if left < div:
                Q = 1
                div = divisor
        if not neg:
            return min(ans,2147483647)
        else:
            return max(-ans,-2147483648)