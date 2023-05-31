#User function Template for python3

class Solution:
    def buildLowestNumber(self, S,N):
        # code here
        arr = []
        k = N
        for digit in S:
            while k > 0 and arr and arr[-1] > digit:
                arr.pop()
                k -= 1
            arr.append(digit)
        arr = arr[:-k] if k > 0 else arr
        return int(''.join(arr))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        S = input()

        solObj = Solution()

        print(solObj.buildLowestNumber(S,N))
# } Driver Code Ends