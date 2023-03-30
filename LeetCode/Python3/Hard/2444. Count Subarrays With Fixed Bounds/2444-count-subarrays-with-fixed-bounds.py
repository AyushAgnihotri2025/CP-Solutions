class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        nm, mm, NM, MM = -1, -1, -1, -1
        ans = 0
        
        for i in range(n):
            if nums[i] < minK:
                nm = i
            if nums[i] == minK:
                mm = i
            if nums[i] > maxK:
                NM = i
            if nums[i] == maxK:
                MM = i
            
            if nums[i] == maxK:
                ans += max(0, mm - max(nm, NM))
            elif nums[i] == minK:
                ans += max(0, MM - max(nm, NM))
            elif mm >= 0 and MM >= 0:
                ans += max(0, min(mm, MM) - max(nm, NM))
        
        return ans