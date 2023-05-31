#User function Template for python3

class Solution:
    def closest3Sum(self, a, n, x):
        # code here
        a.sort()
        ans=float('inf')
        res=0
        for i in range(n-2):
            l=i+1
            r=n-1
            while r>l:
                sum=a[l]+a[r]+a[i]
                if ans>=abs(sum-x):
                    res=sum
                    ans=abs(x-sum)
                        
                if sum>x:
                    r-=1
                elif sum<=x:
                    l+=1
        return res

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
        X = int(input())
        ob = Solution()
        print(ob.closest3Sum(Arr, N, X))
# } Driver Code Ends