class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowel=0
        res =0
        for i in range(0,len(s)):
            if i>=k :
                if s[i-k] in ['a','e','i','o','u']:
                    res -=1
            if s[i] in['a','e','i','o','u']:
                res+=1
            max_vowel = max(max_vowel,res)
            if max_vowel ==k:
                return max_vowel
        return max_vowel