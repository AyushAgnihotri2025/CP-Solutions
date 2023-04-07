#User function Template for python3

class Solution:
    def addMinChar (self, str1):
        # code here 
        i=0
        j=len(str1)-1
        ans=0
        while i<=j:
            if str1[i]!=str1[j]:
                ans+=1
                i=0
                j=len(str1)-1-ans
                continue
            i+=1
            j-=1

        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str1 = input()

        ob = Solution()
        print(ob.addMinChar(str1))

# } Driver Code Ends