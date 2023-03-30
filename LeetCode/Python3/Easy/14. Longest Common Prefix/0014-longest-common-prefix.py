class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = 10**9
        for i in range(len(strs)-1):
            ans = min(ans, min(len(strs[i]), len(strs[i+1])))
            while strs[i][:ans] != strs[i+1][:ans]:
                ans -= 1
            if ans == 0:
                return ""
        return strs[0][:ans]