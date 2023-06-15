#User function Template for python3

class Solution:
    def longestPalin(self, S):
        # code here
        res=""
        s2=0
        if(S==S[::-1]):
            return (S)
        for i in range(len(S)):
            st=''
            s1=0
            for j in range(i,len(S)):
                st+=S[j]
                s1+=1
                if(st==st[::-1]):
                    if(s1>s2):
                        res=st
                        s2=s1
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends