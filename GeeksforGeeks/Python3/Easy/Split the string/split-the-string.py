#User function Template for python3

class Solution:
    def isNotEqual(self,a,b,c,d):
        if(a!=b and a!=c and a!=d and b!=c and b!=d and c!=d):
            return True
        return False
    
    def isPossible (self, S):
        # code here 
        n=len(S)
        if(n<4):
            return 0
        for i in range(1,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if(self.isNotEqual(S[0:i],S[i:j],S[j:k],S[k:])):
                        return 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
       
        s = input()
       
        ob = Solution()
        print(ob.isPossible(s))

# } Driver Code Ends