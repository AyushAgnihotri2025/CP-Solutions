#User function Template for python3

class Solution:
    def isPossible(self, S, N, X, A):
        # code here
        a = [S]
        total = S
        for i in range(N):
            a.append(total + A[i])
            total += a[-1]
        j = N
        while j >= 0 and X > 0:
            if X >= a[j]:
                X -= a[j]
            j -= 1
        return 1 if X == 0 else 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, N, X = [int(y) for y in input().split()]
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        if ob.isPossible(S, N, X, A) == 1:
            print("yes")
        else:
            print("no")
# } Driver Code Ends