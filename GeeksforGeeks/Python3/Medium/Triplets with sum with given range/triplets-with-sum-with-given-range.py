#User function Template for python3

class Solution:
    def countTriplets(self, Arr, N, L, R):
        # code here
        Arr.sort()
        n=len(Arr)
        a=0
        b=0
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                if((Arr[i]+Arr[j]+Arr[k])<=R):
                    a+=(k-j)
                    j+=1
                else:
                    k-=1
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                if((Arr[i]+Arr[j]+Arr[k])<=L-1):
                    b+=(k-j)
                    j+=1
                else:
                    k-=1
        return a-b

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
        L,R = input().split()
        L=int(L)
        R=int(R)
        ob = Solution()
        print(ob.countTriplets(Arr, N, L, R))
# } Driver Code Ends