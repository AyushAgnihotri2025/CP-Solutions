class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        ii,j=min(nums),max(nums)
        while ii<j:
            mid=(ii+j)//2
            total1,total2=0,0
            for i in range(len(nums)):
                total1+=abs(mid-nums[i])*cost[i]
                total2+=abs(mid+1-nums[i])*cost[i]
            if total1<total2:
                j=mid
            else:
                ii=mid+1
        ans=0
        for i in range(len(nums)):
            ans+=abs(ii-nums[i])*cost[i]
        return ans