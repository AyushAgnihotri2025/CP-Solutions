#User function Template for python3

import heapq

def kthDiff( a, n, k):
    a.sort()
    hp=[]
    for i in range(n):
        for j in range(i+1,n):
            heapq.heappush(hp,-(abs(a[i]-a[j])))
            if len(hp)>k:
                heapq.heappop(hp)
    return -(hp[0])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        print(kthDiff(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends