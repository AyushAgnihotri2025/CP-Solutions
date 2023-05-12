#User function Template for python3


class Solution:
    def smallestSumSubarray(self, a, n):
        #Your code here
        ans=1000000000
        sm=0
        for i in range(n):
            sm+=a[i]
            ans=min(ans,sm,a[i])
            if sm>0:
                sm=0
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.smallestSumSubarray(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends