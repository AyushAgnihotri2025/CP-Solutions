class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        permutation = [list(nums)]
        nums_length = len(nums)
        done = False
        while not done:
            print(nums)
            closest = -1
            swap_i = -1
            for i in range(nums_length-2, -1, -1):
                for j in range(i+1, nums_length):
                    if nums[j] > nums[i] and (closest == -1 or nums[j] - nums[i] < closest):
                        closest = nums[j] - nums[i]
                        swap_i = j
                if swap_i != -1:
                    nums[i], nums[swap_i] = nums[swap_i], nums[i]
                    if i+1 < nums_length:
                        nums = nums[:i+1] + sorted(nums[i+1:])
                    permutation.append(list(nums))
                    break
            if swap_i == -1:
                done = True
        return permutation