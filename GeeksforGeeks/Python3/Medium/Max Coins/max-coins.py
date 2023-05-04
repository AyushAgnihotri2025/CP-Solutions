from typing import List
from bisect import bisect_left
from math import inf
class Solution:
    def maxCoins(self, n : int, ranges : List[List[int]]) -> int:
        # code here
        # Sort ranges in ascending order by the end of the range, then start of the range, then value of the range
        ranges.sort(key=lambda x: (x[1], x[0], x[2]))
        # Initialize end list with tuple (0, 0) representing the end of the first range
        end = [(0, 0)]
        res = 0
        for si, ei, ci in ranges:
            # Find the index j of the last range in end that ends before si
            j = bisect_left(end, (si, inf)) - 1
            # Get the end and value of that range
            ej, cj = end[j]
            # Calculate the maximum value of collecting the coins from the current range and the previous ranges
            res = max(res, ci + cj)
            # Append the current range to the end list with the maximum value of coins that can be collected up to this range
            end.append((ei, max(ci, end[-1][1])))
        # Return the maximum value of coins that can be collected
        return res
        



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        ranges=IntMatrix().Input(n, 3)
        
        obj = Solution()
        res = obj.maxCoins(n, ranges)
        
        print(res)
        

# } Driver Code Ends