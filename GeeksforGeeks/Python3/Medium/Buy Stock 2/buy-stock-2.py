#User function Template for python3

class Solution:
    def maximumProfit(self, prices, n):
        #Code here
        result =0
        if(n==1):
            return result
        i=0
        cnt=0
        while i<n-1:
            while ((i<n-1) and (prices[i+1]<=prices[i])):
                i=i+1
            if i==n-1 :
                break
            e=[0,0]
            e[0]=i
            i=i+1
            while ((i<n) and prices[i]>=prices[i-1]):
                i=i+1
            e[1]=i-1
            result+=(prices[e[1]]-prices[e[0]])
            cnt=cnt+1
        if cnt==0:
            return 0
        else:
            return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        prices = list(map(int, input().split()))
        ob = Solution()
        print(ob.maximumProfit(prices, n))
# } Driver Code Ends