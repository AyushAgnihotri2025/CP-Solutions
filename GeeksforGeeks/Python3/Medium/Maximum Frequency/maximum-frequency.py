#User function Template for python3

class Solution:
    def maxFrequency(self, arr, n, k):
        # Code here
        arr.sort()
        presum = [0] * n
        presum[0] = arr[0]
        for i in range(1, n):
            presum[i] = presum[i-1] + arr[i]
        ans = 1
        for i in range(n):
            lo, hi = 0, i-1
            idx = i
            while lo <= hi:
                mi = (lo + hi)//2
                total = presum[i]
                if mi != 0:
                    total -= presum[mi-1]
                if total + k >= (i - mi + 1) * arr[i]:
                    idx = mi
                    hi = mi - 1
                else:
                    lo = mi + 1
            ans = max(ans, i - idx + 1)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        obj = Solution()
        ans = obj.maxFrequency(arr,n,k);
        print(ans)
# } Driver Code Ends