#User function Template for python3
class Solution:
    def sumXOR (self, arr, n) : 
        #Complete the function
        c=0
        for i in range(32):
            s,us=0,0
            for j in arr:
                if j>>i&1:
                    s+=1
                else:
                    us+=1
            c+=(1<<i)*(us*s)
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)


# } Driver Code Ends