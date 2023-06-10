#User function Template for python3

class Solution:
    def findMissing(self,  a, b, n):
        # code here
        res = 0
        for i in range(n):
            res = res ^ a[i] ^ b[i] if i != n-1 else res ^ a[i]
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findMissing(a, b, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends