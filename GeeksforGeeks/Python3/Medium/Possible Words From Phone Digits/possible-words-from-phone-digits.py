#User function Template for python3


class Solution:
    
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a,N):
        #Your code here
        def rec(ind,a,N,curr,res):
            if ind == N:
                res.append(curr)
                return
            val = a[ind]
            lett = d[val]
            for alph in lett:
                curr += alph
                rec(ind+1,a,N,curr,res)
                curr = curr[:-1]

        d = {2:'abc',3:'def',4:'ghi', 5:'jkl', 6: 'mno', 7: 'pqrs', 8:'tuv', 9:'wxyz'}
        res = []
        rec(0,a,N,'',res)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        ob = Solution()
        res = ob.possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends