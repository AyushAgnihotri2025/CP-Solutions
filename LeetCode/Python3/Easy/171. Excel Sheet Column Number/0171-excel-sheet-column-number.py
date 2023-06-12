class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = 0
        for jj in columnTitle:
            s = s * 26 + ord(jj) - ord('A') + 1
        return s