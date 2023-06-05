#User function Template for python3

class Solution:
    #Function to find two repeated elements.
    def twoRepeated(self, arr , N):
        #Your code here
        new_list = set()
        final = []
        for i in arr:
            if i in new_list:
                final.append(i)
            else:
                new_list.add(i)
        return final
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            ans = obj.twoRepeated(A,N)
            print(ans[0], ans[1])
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends