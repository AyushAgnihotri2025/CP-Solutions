#User function Template for python3

class Solution:
    def sumSubarrayMins(self, N, fruits):
        # Code here
        hm={}
        l=0
        r=0
        k=2
        ans=0
        while(r<N):
            if fruits[r] in hm:
                hm[fruits[r]]+=1
            else:
                hm[fruits[r]]=1
            
            while len(hm)>k:
                hm[fruits[l]]-=1
                if hm[fruits[l]]==0:
                    del hm[fruits[l]]
                l+=1
            ans=max(r-l+1,ans)
            r+=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        N = int(input())
        fruits = list(map(int,input().split()))
        ob = Solution()
        res = ob.sumSubarrayMins(N, fruits)
        print(res)
# } Driver Code Ends