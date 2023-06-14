#User function Template for python3

class Solution:
    def graycode(self,n):
        #code here
        self.ans = []
        def recursion(N):
            if N == 1:
                return ["0", "1"]
            temp = recursion(N-1)
            res = []
            for i in range(len(temp)):
                element = "0" + temp[i]
                res.append(element)
            for i in range(len(temp)-1, -1, -1):
                element = "1" + temp[i]
                res.append(element)
            return res
        return recursion(n)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        l=ob.graycode(n)
        
        for x in l:
            print(x, end=" ")
            
        print()
     
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends