#User function Template for python3
import bisect
class Solution:

    def findMaxGuests(self, Entry, Exit, N):
        # code here
        Entry.sort()
        Exit.sort()
        mx=0
        for i in range(N):
            x=bisect.bisect(Entry, Exit[i])
            if x-i > mx:
                mx=x-i
                time=Entry[x-1]
        return [mx,time]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        
        N = int(input())

        entry = [int(x) for x in input().split()]
        exit =  [int(x) for x in input().split()]

        solObj = Solution()
        ans = solObj.findMaxGuests(entry, exit, N) 
        print(ans[0],ans[1])
        

# } Driver Code Ends