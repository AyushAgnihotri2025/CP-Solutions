#User function Template for python3

class Solution:
    def divAndSub(self, N):
        # code here
        if N==1:
            return "Arya"
        elif N==0:
            return "Jon"
        li=[1,0,1,1,1,1,0,0]
        move=[2,3,4,5]
        for i in range(8,N+1):
            count=0
            for j in move:
                if i-j>=0:
                    if li[i-j]==1:
                        count+=1
                    if li[i//j]==1:
                        count+=1
            if count==8:
                li.append(0)
            else:
                li.append(1)
        return "Jon" if li[N]==1 else "Arya"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.divAndSub(N))
# } Driver Code Ends