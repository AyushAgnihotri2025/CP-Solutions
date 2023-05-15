class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        while i > 0 and nums[i]<=nums[i-1]:
            i-=1
        i-=1
        if i<0:
            nums.reverse()
            return
        while j>i and nums[j]<=nums[i]:
            j-=1
        nums[i],nums[j] = nums[j], nums[i]
        k,l = i+1, len(nums)-1
        while k<l:
            nums[k],nums[l] = nums[l], nums[k]
            k+=1
            l-=1