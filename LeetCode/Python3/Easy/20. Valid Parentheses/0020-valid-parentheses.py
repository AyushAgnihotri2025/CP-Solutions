class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in bracket_pairs:
                stack.append(c)
            elif not stack or bracket_pairs[stack.pop()] != c:
                return False
        return not stack