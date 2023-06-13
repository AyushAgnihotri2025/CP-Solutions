#User function Template for python3

class Solution:
    def posIntSol(self,s):
        #code here
        i=0
        pcnt=0
        while s[i]!='=':
            if s[i]=='+':
                pcnt+=1
            i+=1
        r=pcnt+1
        n=''
        i+=1
        while i<len(s):
            n+=s[i]
            i+=1
        n=int(n)
        n=n-r
        if n<=0:
            return 0
        cnt=0
        num=1
        den=1
        while cnt<n:
            num=num*(n+r-1-cnt)
            den=den*(cnt+1)
            cnt+=1
        return num//den

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.posIntSol(s))
# } Driver Code Ends