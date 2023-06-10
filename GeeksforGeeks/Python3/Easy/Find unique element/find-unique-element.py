class Solution:
    def findUnique(self, a, n, k): 
        #Code here
        d1={}
        for i in a:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1

        for i,j in d1.items():
            if j%k!=0:
                return i

#{ 
 # Driver Code Starts
import sys 

if __name__=='__main__':
    T = int(input())

    for _ in range(T):
        n,k=[int(x) for x in input().split()]
        a = [int(x) for x in input().split()]

        print(Solution().findUnique(a,n,k))
# } Driver Code Ends