#User function Template for python3

class Solution:
    def maxValue(self, arr, N):
        # code here 
        a=[]
        b=[]
        for i in range(N):
            a.append(arr[i]+i)
            b.append(-arr[i]+i)

        mx=max(a)
        mn=min(a)
        mx1=max(b)
        mn1=min(b)
        return max(mx-mn,mx1-mn1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxValue(arr,N))
# } Driver Code Ends