#User function Template for python3
#Back-end complete function Template for Python 3
class Solution:
    def maxCandy(self, height, n): 
        # Your code goes here
        s,e=0,n-1
        res=0
        while(s<e):
            res=max(res,min(height[s],height[e])*(e-s-1))
            if height[s]<height[e]:
                s+=1
            else:
                e-=1
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.maxCandy(arr,n))



# } Driver Code Ends