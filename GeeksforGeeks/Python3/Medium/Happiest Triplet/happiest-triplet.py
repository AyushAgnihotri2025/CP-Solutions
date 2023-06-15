#User function Template for python3

class Solution:
    def smallestDifferenceTriplet(self,a,b,c,n):
        #code here.
        a.sort()
        b.sort()
        c.sort()
        n = len(a)
        p1 = p2 = p3 = 0
        ans = float('inf')
        diff = float('inf')  
        while p1 < n and p2 < n and p3 < n:
            mn = min(a[p1], b[p2], c[p3])
            mx = max(a[p1], b[p2], c[p3])
            diff = (mx-mn)
            if diff < ans:
                ans = diff
                px = p1
                py = p2
                pz = p3 
            if a[p1] == mn:
                p1 += 1
            elif b[p2] == mn:
                p2 += 1
            elif c[p3] == mn:
                p3 += 1 
        arr = [a[px], b[py], c[pz]]
        arr.sort(reverse = True)
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ob = Solution()
    ans=ob.smallestDifferenceTriplet(a,b,c,n)
    print(ans[0],ans[1],ans[2])

# } Driver Code Ends