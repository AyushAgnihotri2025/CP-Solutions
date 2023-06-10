#User function Template for python3

class Solution:
    def count3DivNums(self, L, R):
        # code here
        def isPrime(n):
            if n==1:
                return False
            else:
                lim=int(n**0.5)+1
                for i in range(2,lim):
                    if n%i==0:
                        return False
                return True
        c=0
        if L**0.5==int(L**0.5):
            s=int(L**0.5)
        else:
            s=int(L**0.5)+1
        e=int(R**0.5)+1
        for i in range(s,e):
            if isPrime(i):
                c+=1
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        L,R=map(int,input().split())
        
        ob = Solution()
        print(ob.count3DivNums(L,R))
# } Driver Code Ends