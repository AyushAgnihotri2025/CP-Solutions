#User function Template for python3



def stockBuySell(p, n):
    # code here
    start=0;i=1;ans=[]
    while i<n:
        if p[i-1]<p[i]:
            i+=1
        else:
            if start!=i-1:
                ans.append([start,i-1])
            start=i
            i+=1
    if start!=n-1:
        ans.append([start,n-1])
    if not ans:
        print("No Profit")
        return 
    else:
        for i in ans:
            print("("+str(i[0])+' '+str(i[1])+")",end=' ')
        print()


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        price=list(map(int, input().split()))
        stockBuySell(price, n)
# } Driver Code Ends