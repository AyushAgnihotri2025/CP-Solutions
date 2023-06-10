import re

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return re.search(".*".join(list(s)),t)