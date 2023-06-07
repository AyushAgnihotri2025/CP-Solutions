#User function Template for python3

def Ispossible (arr, n, W, P) : 
    # Complete the function
    h=[[0 for i in range(W+1)] for j in range(n+1)]
    for j in range(1,n+1):
        for l in range(1,W+1):
            if l>=arr[j-1][0]:
                h[j][l]=max(arr[j-1][1]+h[j-1][l-arr[j-1][0]],h[j-1][l])
            else:
                h[j][l]=h[j-1][l]
    if h[n][W]<P:
        return -1
    else:
        zonk=h[n][W]
        ans=0
        for i in range(n,0,-1):
            if zonk>0:
                if zonk==h[i-1][W]:
                    continue
                else:
                    zonk=zonk-arr[i-1][1]
                    ans=ans+arr[i-1][0]
                    W=W-arr[i-1][0]
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n, W, P = map(int, input().split())
    arr = []
    for _ in range(0, n):
        ll = list(map(int, input().strip().split()))
        arr.append(ll)
    res = Ispossible(arr, n, W, P)
    if(res == -1):
        print("NO")
    else:
        print("YES " + str(res))






# } Driver Code Ends