#User function Template for python3

class Solution:
    def solve(self,N,dict_hand):
        if N<=2:
            return 1
        if N in dict_hand:
            return dict_hand[N]
        ans = 0
        for i in range(0,N,2):
            ans+=self.solve(i,dict_hand)*self.solve(N-i-2,dict_hand)
            dict_hand[N]=ans
        return ans

    def count(self, N):
        # code here
        dict_hand = {2:1}
        self.solve(N,dict_hand)
        return dict_hand[N]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.count(N))
# } Driver Code Ends