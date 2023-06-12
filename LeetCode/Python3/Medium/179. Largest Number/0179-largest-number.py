class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums,key=lambda x:x / (10 ** len(str(x)) - 1 ), reverse=True)
        str_nums = [str(num) for num in nums]
        res = ''.join(str_nums)
        res = str(int(res))
        return res