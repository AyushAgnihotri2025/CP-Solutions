class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1: 0}
        arr2.sort()
        for a in arr1:
            nextDp = collections.defaultdict(lambda: math.inf)
            for val, steps in dp.items():
                if a > val:
                    nextDp[a] = min(nextDp[a], steps)
                i = bisect_right(arr2, val)
                if i < len(arr2):
                    nextDp[arr2[i]] = min(nextDp[arr2[i]], steps + 1)
            if not nextDp:
                return -1
            dp = nextDp
        return min(dp.values())