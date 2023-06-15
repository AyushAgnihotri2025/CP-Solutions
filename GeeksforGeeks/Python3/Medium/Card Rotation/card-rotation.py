#User function Template for python3

class Solution:
    def rotation (self, N):
        # code here
        l=[-1]*N
        a=[i for i in range(N)]
        j=0
        flag=True
        for i in range(1,N+1):
            k=i
            while(i>=0):
                if l[a[j%len(a)]]==-1:
                    if i!=0:
                        j+=1
                        i-=1
                    else:
                        if l[a[j%len(a)]]==-1:
                            l[a[j%len(a)]]=k
                            c=a[(j+1)%len(a)]
                            a.remove(a[j%len(a)])
                            if c in a:
                                j=a.index(c)
                            break
                        else:
                            flag=False
                            break
            if flag==False:
                break
        if flag==False:
             l=[-1]  
             return l
        return l

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ans = ob.rotation(N);
        print(*ans)


# } Driver Code Ends