#User function Template for python3

class Solution:
    def find_min(self, a, n, k):
        # Code Here
        total = sum(sock // 2 for sock in a)
        if total < k:
            return -1
        ans = 2 * k
        odd = 0
        even = 0
        for i in range(n):
            if a[i] % 2:
                odd += 1
            elif a[i] != 0 and a[i] % 2 == 0:
                even += 1
        return ans + odd + min(even - 1, total - k)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        k = int(input())
        obj = Solution()
        print(obj.find_min(a,n,k))

# } Driver Code Ends