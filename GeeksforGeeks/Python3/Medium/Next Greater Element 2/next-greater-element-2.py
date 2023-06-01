#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def nextGreaterElement(self, N, arr):
        # Code here
        stack = []
        ans = []
        for i in range(2*N-1,-1,-1):
            while len(stack)!=0 and stack[-1]<=arr[i%N]:
                stack.pop()
            if i<N:
                if len(stack)!=0:
                    ans.append(stack[-1])
                else:
                    ans.append(-1)
            stack.append(arr[i%N])
        return reversed(ans)


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.nextGreaterElement(N, arr)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends