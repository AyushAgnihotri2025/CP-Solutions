#User function Template for python3

class Solution:
    def getMin( self, A, B, n):
        # Your code goes here
        if n==1:
            return -1
        x=min(A)
        y=min(B)
        if A.index(x)!=B.index(y):
            return x+y
        else:
            A.remove(x)
            B.remove(y)
            m=min(A)
            n=min(B)
            if x+n<y+m:
                return x+n
            else:
                return y+m
        return -1

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
        print(ob.getMin(a, b, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends