#User function Template for python3

class Solution:
    def LCP(self,arr,n):
        #code here
        arr.sort()
        f=arr[0]
        l=arr[-1]
        ns=''
        a=min(len(f),len(l))
        x=0
        while(x<a):
            if(f[x]==l[x]):
                ns+=f[x]
            else:
                break
            x+=1
        if len(ns)==0:
            return -1
        return ns

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs =int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[ x  for x in input().split()]
        obj=Solution()
        print(obj.LCP(arr,n))
# } Driver Code Ends