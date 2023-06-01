#User function Template for python3

class Solution:
    def getSubstringWithEqual012(self, Str):
        # code here
        maps ={}
        c0 = 0
        c1 = 0
        c2 = 0
        maps[(0,0)] = 1
        ans = 0
        for i in range(0,len(Str)):
            if Str[i]=='0':
                c0 += 1
            elif Str[i]=='1':
                c1 += 1
            else:
                c2 += 1
            if maps.get((c1-c0,c2-c1))!=None:
                ans += maps.get((c1-c0,c2-c1))
                maps[(c1-c0,c2-c1)] += 1
            else:
                maps[(c1-c0,c2-c1)] = 1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.getSubstringWithEqual012(Str))

# } Driver Code Ends