class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        N=len(cuts)

        @lru_cache(None)
        def go(left,right):
            if left+1==right:
                return 0
            best=1e100
            for cut in range(left+1,right):
                cost=cuts[right]-cuts[left]
                best=min(best,go(left,cut)+go(cut,right)+cost)
            return best

        return go(0,N-1)       