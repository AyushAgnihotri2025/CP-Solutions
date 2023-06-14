#User function Template for python3
class Solution:
    def solve(self,inp,out,ans,n):
        if(inp==""):
            if out!="":
                ans.add(out)
            return 
        self.solve(inp[1:],out,ans,n)
        self.solve(inp[1:],out+inp[0],ans,n)
        out=out[:-1]
        
    def allPossibleSubsequences (self, S):
        # code here 
        ans=set()
        n = len(S)
        out=""
        self.solve(S,out,ans,n)
        res=[]
        for i in ans:
            if(i[0] in ('a','e','i','o','u') and i[-1] not in ('a','e','i','o','u')):
                res.append(i)
        res.sort()
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        ans=set()
        ob = Solution()
        ans = ob.allPossibleSubsequences(S)
        if(len(ans)==0):
            print(-1, end = "")
        else:
            for i in ans:
                print(i,end=" ")
        print()
# } Driver Code Ends