#User function Template for python3

class Solution:
    def firstDigit(self, arr, n):
        # code here 
        p=1
        for i in range(n):
            p=p*arr[i]
            d=str(p)
            p=int(d[:6])
        return str(p)[0]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.firstDigit(arr, n))
# } Driver Code Ends