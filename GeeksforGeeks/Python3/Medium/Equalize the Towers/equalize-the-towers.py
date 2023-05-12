class Solution:
    def Bsearch(self, n, h, cost):
        # Your code goes here
        l = 0
        r = 0
        for e in h:
            r = max(r, e)
        for e in h:
            l = min(l, e)
        lc = 0
        pc = 0
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            lc = self.total_cost(mid - 1, h, cost)
            pc = self.total_cost(mid, h, cost)
            if lc >= pc:
                ans = pc
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def total_cost(self, mid, h, Cost):
        total_cost = 0
        for i in range(len(h)):
            total_cost += abs(mid - h[i]) * Cost[i]
        return total_cost


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a=list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        ans=ob.Bsearch(n,a,b)
        print(ans)
# } Driver Code Ends