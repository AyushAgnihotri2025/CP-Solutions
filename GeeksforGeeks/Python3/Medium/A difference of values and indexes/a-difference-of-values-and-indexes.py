class Solution:
    def maxDistance (self, arr, n) : 
        #Complete the function
        cmin = cmax = arr[0]
        ans = 0
        for i in arr[1:]:
            cmin = min(cmin - 1, i)
            cmax = max(cmax + 1, i)
            ans = max(ans, i - cmin, cmax - i)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = Solution().maxDistance(arr, n)
    print(ans)
    





# } Driver Code Ends