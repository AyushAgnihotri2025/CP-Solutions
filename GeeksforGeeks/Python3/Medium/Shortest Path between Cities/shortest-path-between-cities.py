#User function Template for python3

class Solution:
    def shortestPath(self, a, b): 
        # code here
        ans=0
        y=max(a,b)
        x=min(a,b)
        while y>x:
            y=y//2
            ans+=1
            if x>y:
                x=x//2
                ans+=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		x,y = map(int,input().strip().split())
		ob = Solution()
		print(ob.shortestPath(x,y))
# } Driver Code Ends