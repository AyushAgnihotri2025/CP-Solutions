#User function Template for python3

class Solution:
    def lastDigit(self, A, B):
        # code here
        ans = 1
        for i in range(A+1, min(B+1, A+11)):
            ans = (ans * i) % 10
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.lastDigit(A, B))
# } Driver Code Ends