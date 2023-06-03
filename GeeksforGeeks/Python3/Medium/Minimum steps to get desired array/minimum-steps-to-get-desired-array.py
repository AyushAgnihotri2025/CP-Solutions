#User function Template for python3

class Solution:
    def countMinOperations(self, arr, n):
        # code here
        maxop = sub = 0
        for i in range(n):
            operations = 0
            while arr[i] != 0:
                if arr[i]%2 == 0:
                    arr[i] = arr[i] //2
                    operations+=1
                else:
                    arr[i] = arr[i] - 1
                    sub+=1
            maxop = max(maxop, operations)
        return (maxop+sub)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countMinOperations(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends