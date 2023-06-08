#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def solve(self, bt):
        # Code here
        bt.sort()
        cm = 0
        cmm = []
        for i in range(0,len(bt)):
            cm = cm + bt[i]
            cmm.append(cm)
            bt[i] = cmm[i] - bt[i]
        return(sum(bt)//len(bt))


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        bt = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(bt)
        print(res)
# } Driver Code Ends