#User function Template for python3

class Solution: 
    def mostBalloons(self, N, arr):
        # Code here
        if N<3:
            return N
        ans=0
        for i in range(N-1):
            a=arr[i]
            di={}
            curr=1
            for j in range(i+1,N):
                b=arr[j]
                rise=b[1]-a[1]
                run = b[0] - a[0]
                if rise==0 and run==0:
                    curr+=1
                elif rise==0 or run==0:
                    if rise:
                        s=10**9+1
                    else:
                        s=0
                    di[s]=di.get(s,0)+1
                else:
                    s=rise/run
                    di[s]=di.get(s,0)+1
            for i in di.values():
                ans=max(ans,i+curr)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input()) 
        arr=[[] for j in range(N)]
        for j in range(2): 
            inp = [int(i) for i in input().split()] 
            for i in range(N): 
                arr[i].append(inp[i])
        ob = Solution()
        print(ob.mostBalloons(N, arr))
        
        T -= 1
# } Driver Code Ends