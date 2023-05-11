#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,A, B):
        # code here
        ans=[]
        ds=[]
        def solve(index, target, arr, ans, ds):
            if index==len(arr):
                if target==0:
                    ans.append(ds[:])
                return
            if arr[index]<=target:
                ds.append(arr[index])
                solve(index, target-arr[index], arr, ans, ds)
                ds.pop()


            solve(index+1, target, arr, ans, ds)
        A=list(sorted(set(A)))
        solve(0, B, A, ans, ds)
        return ans


#{ 
 # Driver Code Starts.


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        s = int(input())
        ob = Solution()
        result = ob.combinationalSum(a,s)
        if(not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()

# } Driver Code Ends