#User function Template for python3
from collections import Counter

def getMaxandMinProduct( A, Q, N, M):
    # code here
    s, m = Counter(A), max(A)
    ans = [0]*len(Q)
    for i, e in enumerate(Q):
        if e != 0:
            for k in range(e, m+1, e):
                ans[i] += s.get(k, 0)
            
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, m = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        brr = [int(x) for x in input().strip().split()]
        
        ans = getMaxandMinProduct( arr, brr, n, m)
        for i in ans:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends