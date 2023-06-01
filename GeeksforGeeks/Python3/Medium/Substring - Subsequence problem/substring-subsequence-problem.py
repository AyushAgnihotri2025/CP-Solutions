#User function Template for python3

class Solution:
    def getLongestSubsequence(self, A , B):
        # code here 
        l1, l2 = len(A), len(B)
        ans = 0
        for i in range(l2):
            k, count = i, 0
            for j in range(l1):
                if k<l2 and B[k]==A[j]:
                    k, count = k+1, count+1
            ans = max(ans, count)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(str,input().split())
        
        ob = Solution()
        print(ob.getLongestSubsequence(A,B))
# } Driver Code Ends