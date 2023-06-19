#User function Template for python3

class Solution:
    def MaxGcd (self, n, a):
        #complete the function here
        maxi=max(a)
        GCD=[-1]*(maxi+1)
        a.sort()
        Max_GCD=0
        for i in range(1,n):
            if(a[i-1]==a[i]):
                Max_GCD=a[i]
        for i in range(n):
            GCD[a[i]]=1
        for i in range(n):# 2 5 10 12
            for j in range(a[i]+a[i],maxi+1,a[i]):
                if(GCD[j]!=-1):
                    GCD[j]=a[i]
        ans=max(GCD)
        Max_GCD=max(Max_GCD,ans)
        return Max_GCD


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        a = list (map (int, input ().split ()))
        ob = Solution()
        print(ob.MaxGcd(n, a))
# } Driver Code Ends