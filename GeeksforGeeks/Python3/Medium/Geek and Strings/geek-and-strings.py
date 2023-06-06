# User function Template for Python3

class Solution:
    def prefixCount(self, N, Q, li, query):
        # code here
        di={}
        ans=[]
        for word in li[:]:
            for i in range(1,len(word)+1):
                if word[:i] not in di.keys():
                    di[word[:i]]=1
                else:
                    di[word[:i]]+=1
        for word in query:
            if word in di.keys():
                ans.append(di[word])
            else:
                ans.append(0)
        return ans

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        li = []
        for i in range(N):
            s=input().split()
            li.append(s[0])
        Q = int(input())
        query = []
        for i in range(Q):
            s=input().split()
            query.append(s[0])
        
        ob = Solution()
        ans = ob.prefixCount(N, Q, li, query)
        for i in range(Q):
            print(ans[i])
# } Driver Code Ends