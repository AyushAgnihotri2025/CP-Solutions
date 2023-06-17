#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def longestIncreasingSubsequence(self, n, arr):
        # Code here
        dp=[1]*(n)
        hash=[0]*n
        lastind=0
        mx=1
        for curr in range(n):
            hash[curr]=curr
            for prev in range(curr):
                if arr[curr]>arr[prev] and dp[curr]<1+dp[prev]:
                    dp[curr]=1+dp[prev]
                    hash[curr]=prev
            if dp[curr]>mx:
                mx=dp[curr]
                lastind=curr
        ans=[]
        ans.append(arr[lastind])
        while hash[lastind]!=lastind:
            lastind=hash[lastind]
            ans.append(arr[lastind])
        return ans[::-1]


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.longestIncreasingSubsequence(N, arr)
        for val in res:
            print(val, end =' ')
        print()
# } Driver Code Ends