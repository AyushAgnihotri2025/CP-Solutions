#User function Template for python3

class Solution:
    def NumberofLIS(self, n, arr):
        # Code here
        if n == 0:
            return 0
        cnt = [1] * n
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
        max_len = max(dp)
        count = 0
        for i in range(n):
            if dp[i] == max_len:
                count += cnt[i]
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        arr= list(map(int, input().split()))
        ob = Solution()
        print(ob.NumberofLIS(n, arr))
# } Driver Code Ends