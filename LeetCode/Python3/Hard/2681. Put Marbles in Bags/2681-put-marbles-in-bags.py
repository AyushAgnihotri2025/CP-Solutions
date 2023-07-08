class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        p = sorted([weights[i] + weights[i + 1] for i in range(len(weights) - 1)])
        return sum(p[len(p) - k + 1:]) - sum(p[:k - 1])