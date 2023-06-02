#User function Template for python3

from math import factorial

def getAnswer(arr, n, k, x):
    # Your code goes here
    arr.sort()
    count = 0
    f = factorial(k-1)
    j = k-1
    for i in range(n-k+1):
        while j < n and arr[j] - arr[i] <= x:
            j += 1
        if j-i >= k and arr[j-1] - arr[i] <= x:  
            count += factorial(j-i-1)//f//factorial(j-i-k)
    return count % (10**9+7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k, x = sz[0], sz[1], sz[2]
        arr = [int(x) for x in input().strip().split()]
        print( getAnswer(arr, n, k, x) )

        T -= 1


if __name__ == "__main__":
    main()
    
# } Driver Code Ends