class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = Counter(nums)
        l = []
        for i,j in counter.items():
            if j>2:
                l+=[i]*2
            else:
                l+=[i]*j
        nums[:] = l