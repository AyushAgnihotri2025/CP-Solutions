#User function Template for python3

class Solution:
    def findMaxLen(ob, S):
        # code here
        final=[]
        final.append(-1)
        ans=0
        for i in range(len(S)):
            if S[i]=='(':
                final.append(i)
            else:
                final.pop()
                if len(final)==0:
                    final.append(i)
                ans=max(ans,i-final[-1])
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.findMaxLen(S))
# } Driver Code Ends