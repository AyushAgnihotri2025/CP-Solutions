#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        l=c=1
        s=''
        for i in S:
            if i=="I":
                s += ''.join([str(x) for x in range(c, l-1, -1) if str(x) not in s])
                l = c
            c+=1
        s += ''.join([str(c) for c in range(c, l-1, -1) if str(c) not in s])
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends