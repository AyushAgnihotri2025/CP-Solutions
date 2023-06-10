#User function Template for python3

class Solution:
    def printMinimumProduct(self, a, n):
        # Code here
        for i in range(n):
            a[i] = int(a[i])
        return sorted(a)[0]*sorted(a)[1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [x for x in input().strip().split()]
        
        print(Solution().printMinimumProduct(a, n))
        
        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends