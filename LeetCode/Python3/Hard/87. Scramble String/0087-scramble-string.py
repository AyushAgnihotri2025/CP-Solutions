class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False

        memo = {}
        def helper(s1, s2):
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            if s1 == s2:
                memo[(s1, s2)] = True
            elif sorted(s1) != sorted(s2):
                memo[(s1, s2)] = False
            else:
                n = len(s1)
                for i in range(1, n):
                    if (helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:])) or (helper(s1[:i], s2[n-i:]) and helper(s1[i:], s2[:n-i])):
                        memo[(s1, s2)] = True
                        break
                else:
                    memo[(s1, s2)] = False
            return memo[(s1, s2)]
        
        return helper(s1, s2)