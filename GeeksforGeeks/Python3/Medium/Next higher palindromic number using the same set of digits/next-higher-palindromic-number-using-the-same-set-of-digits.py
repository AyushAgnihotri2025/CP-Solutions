#User function Template for python3

class Solution:
    def nextPalin(self,N):
        #code here
        n=len(N)//2
        ns=[int(N[n-1])]
        i=n-2
        while i>=0:
            nn=int(N[i])
            mns=max(ns)
            if nn<mns:
                rn=min(nn+1,mns)
                while rn not in ns:
                    rn+=1
                if rn>mns:
                    rn=mns
                ns.remove(rn)
                ns.append(nn)
                ns.sort()
                rs=str(rn)+"".join([str(nm) for nm in ns])
                N=N[0:i]+rs+N[i+len(rs):len(N)-i-len(ns)-1]+rs[::-1]+N[len(N)-i:]
                return N
            else:
                ns.append(nn)
                i-=1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.nextPalin(s))
# } Driver Code Ends