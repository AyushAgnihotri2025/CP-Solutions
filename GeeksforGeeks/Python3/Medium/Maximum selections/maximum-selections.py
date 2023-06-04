# ranges[i][0] is the start of ith range
# ranges[i][1] is the end of ith range

class Solution:
    def max_non_overlapping(self,ranges):
        # code here
        ranges.sort()
        stack = []
        for start, end in ranges:
            while stack and stack[-1] > end:
                stack.pop()
            if not stack or start >= stack[-1]:
                stack.append(end)
        return len(stack)

#{ 
 # Driver Code Starts
# driver code
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        line = input().strip().split()
        ranges = [[]  for j in range(n)]
        j=0
        for i in range(0,2*n,2):
            ranges[j].append(int(line[i]))
            ranges[j].append(int(line[i+1]))
            j+=1
            
        obj=Solution()
        print( obj.max_non_overlapping(ranges) )
# } Driver Code Ends