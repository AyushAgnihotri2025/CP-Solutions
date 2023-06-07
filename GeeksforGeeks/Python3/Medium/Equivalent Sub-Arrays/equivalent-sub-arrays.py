#User function Template for python3

from collections import defaultdict

class Solution:
    def countDistinctSubarray(self,arr, n): 
        #code here.
        totalele=len(set(arr))
        ans=0
        i=0
        j=0
        dp=defaultdict(int)
        while i<n:
            dp[arr[i]]+=1
            if len(dp)==totalele:
                ans+=n-i
                while j<=i:
                    if dp[arr[j]]==1:
                        dp.pop(arr[j])
                        j+=1
                        break
                    else:
                        dp[arr[j]]-=1
                    if len(dp)==totalele:
                        ans+=n-i
                    j+=1
            i+=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.countDistinctSubarray(a,n))




# } Driver Code Ends