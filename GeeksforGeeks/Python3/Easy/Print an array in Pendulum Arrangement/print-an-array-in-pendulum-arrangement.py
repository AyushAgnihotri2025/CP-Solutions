#User function Template for python3

def pendulumArrangement(arr, n):
    arr.sort()
    a, b = [], []
    for i in range(len(arr)):
        if i%2==0:
            a.append(arr[i])
        else:
            b.append(arr[i])
    a.reverse()
    return a+b

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        answer = pendulumArrangement(arr, n)
        print(*answer)

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends