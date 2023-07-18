#Your Function should return a list containing all possible IP address
#No need to worry about order
class Solution:
    def genIp(self, s):
        #Code here
        res=[]
        if len(s)>12:
            return res
        if len(s)<4:
            return res
        def backtrack(i,dots,curIP):
            if dots ==4 and i==len(s):
                res.append(curIP[:-1])
            if dots>4:
                return
            for j in range(i,min(i+3,len(s))):
                if (int(s[i:j+1])<256 and ((i==j) or s[i]!='0')):
                    backtrack(j+1,dots+1,curIP+s[i:j+1]+'.')
        backtrack(0,0,'')
        return res

#{ 
 # Driver Code Starts
#Main
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        res = Solution().genIp(s)
        res.sort()
        if(len(res)):
            for u in res:
                print(u)
        else:
            print(-1)
# } Driver Code Ends