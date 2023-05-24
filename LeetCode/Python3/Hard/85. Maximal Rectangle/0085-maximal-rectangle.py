class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        maxarea=0
        height=[0]*(len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="1":
                    height[j]+=1
                else:
                    height[j]=0
                stack=[]
            for i,h in enumerate(height):
                start=i
                while stack and h<stack[-1][1]:
                    index,hi=stack.pop()
                    start=index
                    maxarea=max(maxarea,(i-index)*hi)
                stack.append([start,h])
            for i,h in stack:
                maxarea=max(maxarea,(len(height)-i)*h)
        return maxarea