#User function Template for python3

import sys
from typing import List
from collections import deque
 
class Solution:
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        mod = 100000
        queue = deque()
        dist = [sys.maxsize-1]*mod
        dist[start] = 0
        queue.append([start, 0])
        while queue:
            node, steps = queue.popleft()
            for i in arr:
                num = (i*node)%mod
                if steps+1 < dist[num]:
                    dist[num] = steps+1
                    if num == end:
                        return steps+1
                    queue.append([num, steps+1])
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends