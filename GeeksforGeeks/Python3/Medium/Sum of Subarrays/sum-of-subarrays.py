#User function Template for python3

class Solution:
    def subarraySum(self, a, n):
        # code here
        res=0
        for i in range(n):
            res+=a[i]*(i+1)*(n-i)
        return res%(10**9+7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.subarraySum(a, n))
        T -= 1
        
if __name__ == "__main__":
    main()



# } Driver Code Ends