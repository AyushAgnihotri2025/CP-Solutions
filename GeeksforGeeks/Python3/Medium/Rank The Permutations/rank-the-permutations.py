#User function Template for python3

class Solution:
    def rank(self, S):
        # code here
        n=len(S)
        f=[0]*26
        for i in range(n):
            if f[ord(S[i])-ord("a")]==1:
                return 0
            f[ord(S[i])-ord("a")]+=1
        fact=[0 for i in range(n+1)]
        fact[0]=1
        fact[1]=1
        res=1
        for i in range(2,n):
            fact[i]=i*fact[i-1]
        for i in range(n):
            c=0
            for j in range(ord(S[i])-ord("a")):
                c+=f[j]
            res+=c*fact[n-1-i]
            f[ord(S[i])-ord("a")]-=1
        return res%1000003

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        
        ob = Solution()
        print(ob.rank(S))
# } Driver Code Ends