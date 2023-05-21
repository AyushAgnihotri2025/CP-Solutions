#User function Template for python3

class Solution:
    def longestPalindrome(self, S):
        # code here
        l=[S[i:j] for i in range(len(S)) for j in range(i+1,len(S)+1)]
        m=[]
        for i in l:
            if i==i[::-1] :
                m.append(i)
        return(max(m,key=len))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.longestPalindrome(S))
# } Driver Code Ends