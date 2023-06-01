#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def rec(self,i,n,s,l):
        if i==n:
            l.append(s)
            return l
        s+="0"
        self.rec(i+1,n,s,l)
        s=s[0:len(s)-1:1]
        if s and s[-1]!="1" or s=="":
            s+="1"
            self.rec(i+1,n,s,l)
        return l

    def generateBinaryStrings(self, n):
        # Code here
        return self.rec(0,n,"",[])

#{ 
 # Driver Code Starts.
from sys import stdout
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        res = ob.generateBinaryStrings(N)
        for binaryString in res:
            print(binaryString, end = ' ')
        print()
# } Driver Code Ends