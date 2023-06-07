#User function Template for python3

class Solution:
    def countSubarrays(self, a,n,L,R): 
        # Complete the function
        fp,lp =0,0
        ans = 0
        prev = 0
        while(lp<n):
            if a[lp]>=L and a[lp] <= R:
                prev = lp-fp+1
            elif a[lp]>R:
                prev = 0
                fp = lp+1
            lp+=1
            ans += prev
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    n,l,r = map(int, input().strip().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    v = ob.countSubarrays(arr, n, l, r)
    print(v)
    
# } Driver Code Ends