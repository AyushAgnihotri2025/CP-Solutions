#User function Template for python3

def inversePermutation (arr, n) : 
    #Complete the function
    li = [0]*n
    for i in range(n):
        li[arr[i]-1] = i+1
    return li

#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = inversePermutation(arr, n)
    print(*ans)
    





# } Driver Code Ends