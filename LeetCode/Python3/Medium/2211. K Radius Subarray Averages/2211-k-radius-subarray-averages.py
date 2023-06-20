class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0: return nums
        result = [-1]*len(nums)
        if k > len(nums): return result
        left, mid, right = 0, k, 2*k
        left_sum = sum(nums[left:mid])
        right_sum = sum(nums[mid+1: right+1])
        while right < len(nums):
            result[mid] = int((left_sum + right_sum + nums[mid])/(2*k+1)) 
            left_sum -= nums[left]
            left += 1
            left_sum += nums[mid]
            right_sum -= nums[mid+1]
            right += 1
            if right <= len(nums)-1: right_sum += nums[right]
            mid += 1
        return result