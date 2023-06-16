#User function Template for python3

class Solution:
    def printMissingIntervals(self, a , n):
        # code here
        sp = 0
        ans = []
        for i in a:
            if(i == sp):
                sp = i + 1
            else:
                ans.append(sp)
                ans.append(i - 1)
                sp = i + 1
        if(sp <= 99999):
            ans.append(sp)
            ans.append(99999)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        a=list(map(int,input().split()))
        
        ob = Solution()
        l = ob.printMissingIntervals(a , n)
        
        for i in range(0,len(l),2):
            if l[i]==l[i+1]:
                print(l[i],end="")
            else:
                print(l[i],end="")
                print("-",end="")
                print(l[i+1],end="")
            if i!=len(l)-2:
                print(",",end="")
        print()
# } Driver Code Ends