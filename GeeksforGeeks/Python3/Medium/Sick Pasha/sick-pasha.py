#User function Template for python3

def QueryComputation (n, arr, k, q, queries) : 
    # Complete the function
    ma = 200001
    cnt = [0] * ma
    for a in arr:
        cnt[a[0]-1] -= 1
        cnt[a[1]] += 1
    for i in range(ma-2, -1, -1):
        cnt[i] += cnt[i+1]
    ans = []
    for qu in queries:
        ans.append(cnt[qu] >= k)
    return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = []
    for i in range(0, n):
        ll = list(map(int, input().strip().split()))
        arr.append(ll)
    k, q = map(int, input().split())
    queries = []
    for i in range(0, q):
        queries.append(int(input()))
    ans = QueryComputation(n, arr, k, q, queries)
    for i in ans:
        if(i == True):
            print("Yes")
        else:
            print("No")
        
    
# } Driver Code Ends