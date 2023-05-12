#User function Template for python3

class Solution:
    def divisors(self, val):
        ans = []
        for i in range(1, int(val ** 0.5) + 1):
            if val % i == 0:
                if val // i == i:
                    ans.append(i)
                else:
                    ans.append(i)
                    ans.append(val // i)
        return ans

    def printPairs(self, a, n, h):
        #code here.
        a.sort()
        count = 0
        _set = set(a)
        k = h
        for i in range(n):
            val = a[i]
            if k in _set and val > k:
                count += 1
            if val >= k:
                arr = self.divisors(val - k)
                for j in arr:
                    if j in _set and val % j == k and val != j:
                        count += 1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.printPairs(a,n,k)
    print(ans)

# } Driver Code Ends