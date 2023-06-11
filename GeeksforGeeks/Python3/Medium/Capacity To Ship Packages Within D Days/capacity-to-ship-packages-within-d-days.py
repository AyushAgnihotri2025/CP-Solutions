#User function Template for python3

class Solution:
    def leastWeightCapacity(self, arr, N, D):
        # code here
        l=max(arr)
        h=sum(arr)
        while l<h:
            m=(l+h)//2
            c=0
            d=1
            for i in arr:
                if c+i>m:
                    d+=1
                    c=0
                c+=i
            if d>D:
                l=m+1
            else:
                h=m
        return l

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        D=int(input())
        
        ob = Solution()
        print(ob.leastWeightCapacity(arr,N,D))
# } Driver Code Ends