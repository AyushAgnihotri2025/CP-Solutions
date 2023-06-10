class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        pos,neg=[],[]
        if len(nums)==1:
            return nums[0]
        for x in nums:
            if x>0:
                pos.append(x)
            elif x<0:
                neg.append(-x)
        neg.sort(reverse=True)
        if len(neg)%2==1:
            neg.pop()
        if len(neg)==0 and len(pos)==0:
            return 0
        else:
            res=1
            for x in neg: res*=x
            for x in pos: res*=x
            return res