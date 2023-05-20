#User function Template for python3

class Solution:
    def lengthOfLongestAP(self, A, n):
        # code here
        a=A
        if n<=2:
            return n
        ans=0
        dp=[{} for i in range(n+1)]
        for i in range(1,n):
            for j in range(0,i):
                diff=a[i]-a[j]
                cnt=1
                if diff in dp[j]:
                    cnt=dp[j][diff]
                dp[i][diff]=1+cnt
                ans=max(ans,dp[i][diff])
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        A = list(map(int, input().split()))
        ob = Solution()
        ans = ob.lengthOfLongestAP(A, n)
        print(ans)
        tc -= 1

# } Driver Code Ends