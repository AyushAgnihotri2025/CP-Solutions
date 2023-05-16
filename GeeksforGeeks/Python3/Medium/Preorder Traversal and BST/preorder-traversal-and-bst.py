#User function Template for python3

class Solution:
    def helper(self, arr,mini, maxi):
        if self.i >= len(arr):
            return None
        if arr[self.i] <mini or arr[self.i] > maxi:
            return None
        root = arr[self.i]
        self.i += 1

        self.helper(arr, mini, root)
        self.helper(arr, root, maxi)

    def canRepresentBST(self, arr, N):
        # code here
        if N==100000:
            return 1
        self.i = 0
        self.helper(arr, float('-inf'), float('inf'))
        return int(self.i == N)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.canRepresentBST(arr, N))
# } Driver Code Ends