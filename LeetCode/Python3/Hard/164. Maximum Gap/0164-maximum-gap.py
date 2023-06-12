class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        count=0
        x=len(nums)
        nums.sort()
        if x<2:
            return 0
        if x==2:
            return (nums[1]-nums[0])
        for i in range(1,len(nums)-1):
            max1=nums[i+1]-nums[i]
            if(max1>count):
                count=max1
        return count