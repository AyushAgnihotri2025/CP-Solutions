import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        pairs = [0] * n

        sorted_potions = sorted(potions)

        for i in range(n):
            idx = bisect.bisect_left(sorted_potions, (success + spells[i] - 1) // spells[i])
            pairs[i] = m - idx

        return pairs