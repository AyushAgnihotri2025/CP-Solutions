#User function Template for python3

class Solution:
    def solve(self, arr, n):
        # code here
        arr.sort()
        first,second="",""
        for i in range(n):
            if i%2==0:
                first+=str(arr[i])
            else:
                second+=str(arr[i])
        if first=="":
            first="0"
        if second=="":
            second="0"
        return int(first)+int(second)

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.solve(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends