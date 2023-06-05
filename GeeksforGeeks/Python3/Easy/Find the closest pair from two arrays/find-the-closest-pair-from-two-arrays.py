#User function Template for python3

class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        #code here
        l=0
        r=m-1
        cl=9999
        while(l<n and r>=0):
            sm=arr[l]+brr[r]
            if(abs(sm-x)<=cl):
                cl=abs(sm-x)
                bl,br=l,r
                if(abs(sm-x)==0):
                    return([arr[bl],brr[br]])
            if(sm>x):
                r-=1
            else:
                l+=1
        if(r==-1):
            r=0
        if(l==n):
            l-=1
        return([arr[bl],brr[br]])
#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    x = int(input())
    ob = Solution()
    ans = ob.printClosest(arr, brr, n, m, x)
    print(abs(ans[0]+ans[1] - x))
# } Driver Code Ends