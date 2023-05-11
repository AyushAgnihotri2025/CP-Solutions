class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [0 for i in range(len(height))]
        maxright = [0 for i in range(len(height))]
        ml = mr = 0
        for i in range(len(height)):
            ml = max(ml, height[i])
            maxleft[i] = ml
        for i in range(len(height)-1, -1, -1):
            mr = max(mr, height[i])
            maxright[i] = mr
        
        res = 0
        for i in range(len(height)):
            res += max( min(maxleft[i],maxright[i])-height[i], 0)
            
        return res