#User function Template for python3

class Solution:
    def convert(self, Str, n):
        # code here
        if n == 1:
            return Str
        arr = [''] * n
        row, isDown = 0, True
        for char in Str:
            arr[row] += char
            if isDown:
                row += 1
            else:
                row -= 1
            if row == n - 1:
                isDown = False
            elif row == 0:
                isDown = True
        return "".join(arr)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()
        n = int(input())

        solObj = Solution()

        print(solObj.convert(Str,n))
# } Driver Code Ends