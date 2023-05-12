#User function Template for python3

from bisect import bisect_left

def maxModValue(arr, n):  
    # code here
    arr.sort()
    ans = 0
    for i in range(n):
        for j in range(2 * arr[i], arr[i] + arr[n - 1], arr[i]):
            ind = bisect_left(arr, j) - 1
            ans = max(ans, arr[ind] % arr[i])
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    print(maxModValue(a,n))







# } Driver Code Ends