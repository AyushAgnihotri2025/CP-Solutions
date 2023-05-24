#User function Template for python3

class Solution:
    def countOfSubstrings(self, S, K):
        # code here 
        count=0
        dic=dict()
        i,j=0,0
        while j<len(S):
            if S[j] in dic:
                dic[S[j]]+=1
            else:
                dic[S[j]]=1
            if j-i+1==K:
                if len(dic)==K-1:
                    count+=1
            elif j-i+1>K:
                dic[S[i]]-=1
                if dic[S[i]]==0:
                    del dic[S[i]]
                i+=1
                if len(dic)==K-1:
                    count+=1
        
            j+=1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        K=int(input())
        
        ob = Solution()
        print(ob.countOfSubstrings(S,K))
# } Driver Code Ends