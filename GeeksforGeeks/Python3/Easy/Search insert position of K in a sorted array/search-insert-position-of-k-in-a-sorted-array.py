#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        # code here
        b=N
        Arr.sort()
        for i in Arr:
            if(k==i):
                b=Arr.index(k)
        for i in Arr:
            if(k>i) :
                c=Arr.index(i)+1
        if(b<N):
            return b
        elif(Arr[0]<k<Arr[N-1]) :
            return c
        elif (k>Arr[N-1]):
            return N
        else:
            return 0
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends