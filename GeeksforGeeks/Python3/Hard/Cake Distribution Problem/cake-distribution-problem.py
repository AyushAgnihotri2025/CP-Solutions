#User function Template for python3

class Solution():
    def maxSweetness(self, sweetness, n, k):
        #your code goes here
        l = 1
        r = 10**9
        ans = 0
        while l <= r:
            m = (l+r)//2
            p = 0
            cur = 0
            for i in range(0,n):
                cur += sweetness[i]
                if cur >= m:
                    p += 1
                    cur = 0
            if p >= k+1:
                ans = m
                l = m+1
            else:
                r = m-1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n,k = map(int, input().split())
    sweetness = [int(i) for i in input().split()]
    print(Solution().maxSweetness(sweetness, n,k))
# } Driver Code Ends