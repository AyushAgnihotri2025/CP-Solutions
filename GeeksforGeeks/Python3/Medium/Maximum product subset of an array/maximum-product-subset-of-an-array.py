class Solution:
    def findMaxProduct(self,a, n):
        #Write your code here
        mod=1000000007
        if len(a)==1:
            return a[0]
        zcount=0
        ncount=0
        prod=1
        mxneg=-99999
        
        for i in a:
            if i==0:
                zcount+=1
                continue
            if i<0:
                ncount+=1
                mxneg=max(mxneg,i)
            prod*=i
        if zcount==n:
            return 0
        if ncount==1 and ncount+zcount==n:
            return 0
        if ncount%2==0:
            return prod%mod
        else:
            return (prod//mxneg)%mod



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        a = list(map(int, input().split()))
        obj=Solution()
        ans=obj.findMaxProduct(a, n)
        print(ans)
# } Driver Code Ends