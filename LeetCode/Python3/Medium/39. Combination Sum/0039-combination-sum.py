class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        if not candidates:
            return []
        self.helper(candidates, 0, [], target)
        return self.res

    def helper(self, candidates, start, items, target):
        if target == 0:
            self.res.append(items)
        for i in range(start,len(candidates)):
            if candidates[i]>target:
                return
            self.helper(candidates, i, items+[candidates[i]], target-candidates[i])