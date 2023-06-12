class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            return [str(nums[0])]
        ans = []
        i,j = 0,1
        while j < len(nums):
            while j<len(nums) and nums[i] - nums[j] == i-j:
                j += 1
            if i!=j-1:
                ans.append(str(nums[i])+'->'+str(nums[j-1]))
            else:
                ans.append(str(nums[i]))
            i = j
            j += 1
            if i == len(nums)-1:
                ans.append(str(nums[i]))
                break
        return ans