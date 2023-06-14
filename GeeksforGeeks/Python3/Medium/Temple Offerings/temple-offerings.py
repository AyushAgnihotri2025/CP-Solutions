#User function Template for python3

class Solution:
    def offerings(self, N, arr):
        # code here
        ans = [1 for i in range(N)]
        for i in range(1, N):
            if arr[i]>arr[i-1]:
                ans[i] =ans[i-1] + 1
        for i in range(N-2, -1, -1):
            if arr[i]>arr[i+1] and ans[i]<=ans[i+1]:
                ans[i] = ans[i+1] + 1
        return sum(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.offerings(N, arr))
# } Driver Code Ends