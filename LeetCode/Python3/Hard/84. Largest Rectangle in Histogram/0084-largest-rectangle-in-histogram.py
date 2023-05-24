class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0
        for i,v in enumerate(heights):
            start=i
            while stack and stack[-1][1]>v:
                index,height=stack.pop()
                maxarea=max(maxarea,(i-index)*height)
                start=index
            stack.append((start,v))
        for i,h in stack:
            maxarea=max(maxarea,h*(len(heights)-i))
        return maxarea