#User function Template for python3

class Solution:
    def nthCharacter(self, S, R, N):
        # code here
        f = 1
        fl = 0
        while R:
            fl = N >> 1
            if 2 * fl == N: f = int(not(f ^ 1))
            else: f = int(not(f ^ 0))
            N >>= 1
            R -= 1
        if f == 0: return str(int(not int(S[fl])))
        else: return S[fl]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends