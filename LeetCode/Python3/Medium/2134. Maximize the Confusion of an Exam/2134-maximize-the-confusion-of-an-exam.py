class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        freq = defaultdict(int)
        max_freq = max_length = 0
        left = right = 0
        while right < len(answerKey):
            freq[answerKey[right]] += 1
            max_freq = max(max_freq, freq[answerKey[right]])
            if (right - left + 1) - max_freq <= k:
                max_length = max(max_length, right - left + 1)
            else:
                freq[answerKey[left]] -= 1
                left += 1
            right += 1
        return max_length