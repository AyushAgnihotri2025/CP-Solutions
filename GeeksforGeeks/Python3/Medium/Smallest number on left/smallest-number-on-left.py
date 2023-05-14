# User function Template for Python3

class Solution:
    def leftSmaller(self, n, a):
        # code here

        stack = []
        ans = []
        for i in range(n):
            while stack and a[i] <= stack[-1]:
                stack.pop()
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(a[i])
        return ans

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])
        
        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in(ans):
            print(u,end = " ")
        print()
# } Driver Code Ends