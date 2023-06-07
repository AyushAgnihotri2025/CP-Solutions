#User function Template for python3

def maxSumWithK( a, n, k):
    maxSum = [0 for i in range(n)]
    maxSum[0] = a[0]
    curr_sum = a[0]
    for i in range(1,n):
        curr_sum = max(a[i],curr_sum+a[i])
        maxSum[i] = curr_sum
    sum = 0
    for i in range(k):
        sum += a[i]
    result = sum
    for i in range(k,n):
        sum += a[i] - a[i-k]
        result = max(sum,result)
        result = max(result,sum + maxSum[i-k])
    return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        print(maxSumWithK(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends