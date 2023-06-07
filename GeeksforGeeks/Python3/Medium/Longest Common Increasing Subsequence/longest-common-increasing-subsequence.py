#User function Template for python3

class Solution:
    def LCIS(self, arr1, n, arr2, m):
        # code here
        table = [0] * m
        for j in range(m):
            table[j] = 0
        for i in range(n):
            current = 0
            for j in range(m):
                if (arr1[i] == arr2[j]):
                    if (current + 1 > table[j]):
                        table[j] = current + 1
                if (arr1[i] > arr2[j]):
                    if (table[j] > current):
                        current = table[j]
        result = 0
        for i in range(m):
            if (table[i] > result):
                result = table[i]
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        m = int(input())
        arr1 = list(map(int, input().strip().split()))
        n = int(input())
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.LCIS(arr1, m, arr2, n)
        print(ans)
        tc -= 1

# } Driver Code Ends