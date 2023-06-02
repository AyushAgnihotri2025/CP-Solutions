#User function Template for python3

import heapq

def maximised_height (arr, n, m) : 
    #Complete the function
    heapq.heapify(arr)
    count = 1
    while arr and m >= count:
        item = heapq.heappop(arr)
        while arr and item < arr[0] and m >= count:
            item += 1
            m -= count
        count += 1
    if not arr:        
        count -= 1
    while m >= count:
        item += 1
        m -= count
    return item

#{ 
 # Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    ans = maximised_height(arr, n, m)
    print(ans)
    





# } Driver Code Ends