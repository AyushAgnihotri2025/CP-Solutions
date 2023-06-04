#User function Template for python3

def reaching_height(n, arr): 
    # Complete the function
    arr.sort()
    lst = []
    if arr.count(arr[0])==n and n>1:
       return [-1]
    else:
       for i in range(0,n//2):
           x = i+1
           lst.extend([arr[-x],arr[i]])
       if n%2 != 0:
           lst.append(arr[n//2])
       return lst

#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = reaching_height(n, arr)
    if(len(ans) == 1 and ans[0] == -1):
        print("Not Possible")
    else:
        print(*ans)
# } Driver Code Ends