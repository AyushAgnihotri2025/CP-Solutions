from typing import List

class Solution:
    def minTime(self, n : int, locations : List[int], types : List[int]) -> int:
        # code here
        d={}
        for i in range(len(types)):
            if(types[i] in d):
                d[types[i]]=[min(d[types[i]][0],locations[i]),max(d[types[i]][1],locations[i])]
            else:
                d[types[i]]=[locations[i],locations[i]]
        dp=[[0,0] for _ in range(len(d))]
        m1=min(d)
        m2=max(d)
        dp[0][0]=abs(d[m1][0])+abs(d[m1][1]-d[m1][0])
        dp[0][1]=abs(d[m1][1])+abs(d[m1][1]-d[m1][0])
        j=1
        prv=m1
        for i in range(m1+1,m2+1):
            if(i in d):
                dp[j][0]=min(abs(d[prv][0]-d[i][0])+dp[j-1][1],abs(d[prv][1]-d[i][0])+dp[j-1][0])+abs(d[i][1]-d[i][0])
                dp[j][1]=min(abs(d[prv][0]-d[i][1])+dp[j-1][1],abs(d[prv][1]-d[i][1])+dp[j-1][0])+abs(d[i][1]-d[i][0])
                prv=i
                j+=1
        dp[j-1][0]+=abs(d[prv][1])
        dp[j-1][1]+=abs(d[prv][0])
        return min(dp[j-1])

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        locations=IntArray().Input(n)
        
        
        types=IntArray().Input(n)
        
        obj = Solution()
        res = obj.minTime(n, locations, types)
        
        print(res)
        

# } Driver Code Ends