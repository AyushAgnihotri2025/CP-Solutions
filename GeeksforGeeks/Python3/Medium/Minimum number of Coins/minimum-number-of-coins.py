#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here
        a=[1,2,5,10,20,50,100,200,500,2000]
        l=[]
        i=len(a)-1
        while N!=0 and i>=0:
            if a[i]>N:
                i-=1
            else:
                N-=a[i]
                l.append(a[i])
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends