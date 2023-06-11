class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        def dfs(s):
            if s in memo:
                return memo[s]
            if not s:
                return []
            res = []
            for i in range(1, len(s) + 1):
                if s[:i] in word_set:
                    right_sents = dfs(s[i:])
                    if right_sents:
                        for right_sent in right_sents:
                            res.append(s[:i] + " " + right_sent)
                    elif not s[i:]:
                        res.append(s[:i])
            memo[s] = res
            return res
        return dfs(s)