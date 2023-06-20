#User function Template for python3

class Solution:
    def binarySearchable(self, Arr, n):
        # code here 
        left = [0]*n
        right = [0]*n
        mx  = -float("inf")
        for i in range(n):
            left[i] = mx
            mx = max(mx, Arr[i])
        mn = float("inf")
        for i in range(n-1, -1, -1):
            right[i] = mn
            mn = min(mn, Arr[i])
        cnt = 0
        for i in range(n):
            if Arr[i]> left[i] and Arr[i] < right[i]:
                cnt += 1
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        Arr=list(map(int,input().split()))
        ob = Solution()
        print(ob.binarySearchable(Arr,n))

# } Driver Code Ends