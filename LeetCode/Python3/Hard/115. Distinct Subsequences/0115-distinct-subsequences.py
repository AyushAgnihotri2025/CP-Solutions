class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls = len(s)
        lt = len(t)
        if ls == lt:
            if s == t:
                return 1
            else:
                return 0
        if lt > ls:
            return 0
        deletes_possible = ls - lt
        @cache
        def dp(ci, cj, remains):
            if ci == len(s):
                if cj == len(t):
                    return 1
                else:
                    return 0
            if cj == len(t):
                return 1
            if remains > 0:
                if s[ci] == t[cj]:
                    return dp(ci+1, cj, remains - 1) + dp(ci+1, cj + 1, remains)
                else:
                    return dp(ci+1, cj, remains - 1)
            else:
                if s[ci] == t[cj]:
                    return dp(ci+1, cj+1, remains) 
                else:
                    return 0
        return dp(0, 0, deletes_possible)