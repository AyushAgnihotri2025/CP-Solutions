#User function Template for python3

class Solution:
    def longestCommon(self, N, M):
        # code here
        d=[]
        e=[]
        while(N>0):
            d.append(N%2)
            N//=2
        while(M>0):
            e.append(M%2)
            M//=2
        a1={}
        for i in range(len(d)):
            c=0
            p=1
            s=''
            for j in range(i,len(d)):
                s+=str(d[j])
                a1[s]=1
        res=0
        c2=0
        for i in range(len(e)):
            c=0
            p=1
            s=''
            c1=0
            for j in range(i,len(e)):
                c+=(p*(e[j]))
                p*=2
                s+=str(e[j])
                c1+=1
                if s in a1:
                    # print(s)
                    if(c1>c2):
                        res=c
                        c2=c1
                    elif c1==c2:
                        res=max(res,c)
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        
        N,M=input().split()
        N=int(N)
        M=int(M)

        solObj = Solution()

        ans = solObj.longestCommon(N, M)

        print(ans)
# } Driver Code Ends