class Solution:
    def inversion_count(self, n, k, arr):
        # Your code goes here
        ans = 0
        for i in range(n):
            for j in range(i+1, min(n, i+k)):
                if arr[i] > arr[j]:
                    ans += min(k - (j - i), i + 1, n - k + 1, n - j)
        return ans

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l = list(map(int, input().split()))
        n=l[0]
        k=l[1]
        a=list(map(int,input().split()))
        ob = Solution()
        ans=ob.inversion_count(n,k,a)
        print(ans)
# } Driver Code Ends