#User function Template for python3
class Solution:
    def findAndReplace(self, S, Q, index, sources, targets):
        # code here
        index.reverse()
        sources.reverse()
        targets.reverse()
        for ind,so,tar in zip(index,sources,targets):
            if (S[ind:ind+len(so)] == so):
                S = S[0:ind]+tar+S[ind+len(so):]
        return S

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        Q=int(input())
        index=list(map(int,input().split()))
        sources=list(map(str,input().split()))
        targets=list(map(str,input().split()))
        
        ob = Solution()
        print(ob.findAndReplace(S,Q,index,sources,targets))
# } Driver Code Ends