#User function Template for python3
class Solution:
    def find3number(self,A, n):
        # code here
        min_arr = (n+1)*[0]
        min_idx = 0
        for i in range(1,n):
            if A[i] <= A[min_idx]:
                min_arr[i] = -1
                min_idx = i
            else:
                min_arr[i] = min_idx
        max_arr = (n+1)*[0]
        max_idx = n-1
        for i in range(n-2,-1,-1):
            if A[i]>= A[max_idx]:
                max_idx = i
                max_arr[i] = -1
            else:
                max_arr[i] = max_idx
        for i in range(n):
            if max_arr[i]!=-1 and min_arr[i]!=-1:
                if A[min_arr[i]]<A[i] and A[i]<A[max_arr[i]]:
                    return [A[min_arr[i]],A[i],A[max_arr[i]]]
                else:
                    continue
        return []
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(100000)

def isSubSeq(arr, lis, n, m):
    if m==0:
        return True
    if n==0:
        return False
    if arr[n-1]==lis[m-1]:
        return isSubSeq(arr, lis, n-1, m-1)
    return isSubSeq(arr, lis, n-1, m)

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().strip().split()))
    lis = Solution().find3number(arr, n)
    # print(lis)
    # print(isSubSeq(arr, lis, n, len(lis)))
    if len(lis)!=0 and len(lis)!=3:
        print(-1)
        continue
    if len(lis)==0:
        print(0)
    elif lis[0]<lis[1] and lis[1]<lis[2] and isSubSeq(arr, lis, n, len(lis)):
        print(1)
    else:
        print(-1)
        
# } Driver Code Ends