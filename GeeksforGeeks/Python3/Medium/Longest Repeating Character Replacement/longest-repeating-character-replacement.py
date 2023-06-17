#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def characterReplacement(self, S, K):
        # Code here
        left,n,charDict,maxCount,ans=0,len(S),{},0,0
        for right in range(n):
            if S[right] in charDict:
                charDict[S[right]]+=1
            else:
                charDict[S[right]]=1
            maxCount = max(maxCount, charDict[S[right]])
            while (right-left+1) - maxCount > K:
                charDict[S[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range(t):
        S = input().strip()
        K = int(input())
        ob = Solution()
        res = ob.characterReplacement(S, K)
        print(res)
# } Driver Code Ends