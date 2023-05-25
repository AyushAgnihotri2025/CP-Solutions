#User function Template for python3

class Solution:
    def InternalCount(self, p, q, r):
        #code here
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)

        def area(a,b,c):
            x1,y1 = a[0],a[1]
            x2,y2 = b[0],b[1]
            x3,y3 = c[0],c[1]
            temp = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
            return temp

        def points(p,q):
            if p[1] == q[1]:
                return abs(p[0] - q[0]) -1
            if p[0] == q[0]:
                return abs(p[1] - q[1]) -1
            return gcd(abs(p[0]-q[0]),abs(p[1]-q[1])) - 1

        count = 3
        count += points(p,q)
        count += points(p,r)
        count += points(q,r)
        b = count
        a = area(p,q,r)
        res = ((a - b) + 2)//2
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        p=[0]*2
        q=[0]*2
        r=[0]*2
        p[0],p[1],q[0],q[1],r[0],r[1]=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.InternalCount(p,q,r);
        print(ans)
# } Driver Code Ends