class Solution:
    def partitionString(self, s: str) -> int:
        result, left = 1, 0
        lookup = {}
        for i, x in enumerate(s):
            if x in lookup and lookup[x] >= left:
                left = i
                result += 1
            lookup[x] = i
        return result