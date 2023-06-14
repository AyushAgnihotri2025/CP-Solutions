#User function Template for python3

class Solution:
    def sevenSegments(self, S, N):
        # code here
        segs = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5]
        total = sum(segs[int(S[i])] for i in range(N))
        ans = ['0'] * N
        for i in range(N):
            if total == 2 * (N - i):
                ans[i] = '1'
                total -= 2
            elif total == 7 * (N - i):
                ans[i] = '8'
                total -= 7
            elif total - 6 >= 2 * (N - i - 1) and total - 6 <= 7 * (N - i - 1):
                ans[i] = '0'
                total -= 6
            elif total - 2 <= 7 * (N - i - 1):
                ans[i] = '1'
                total -= 2
            elif total - 3 <= 7 * (N - i - 1):
                ans[i] = '7'
                total -= 3
            elif total - 4 <= 7 * (N - i - 1):
                ans[i] = '4'
                total -= 4
            elif total - 5 <= 7 * (N - i - 1):
                total -= 5
                ans[i] = '2'
        return ''.join(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        S=input()
        
        ob = Solution()
        print(ob.sevenSegments(S,N))
# } Driver Code Ends