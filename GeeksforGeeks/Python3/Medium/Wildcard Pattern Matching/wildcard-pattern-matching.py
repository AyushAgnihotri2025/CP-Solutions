# your task is to complete this helperction
# helperction should return True/False or 1/0
# str1: pattern
# str2: text
class Solution:
    def wildCard(self,pattern, string):
        # Code here

        dp={}

        def helper(i,j):
            if i==len(pattern) and j==len(string):
                return True

            if i==len(pattern):
                return False

            if j==len(string):
                if pattern[i]=="*":
                    while i< len(pattern) and pattern[i]=="*":
                        i+=1
                    if i==len(pattern):
                        return True
                    else:
                        return False
                else:
                    return False

            if (i,j) in dp:
                return dp[(i,j)]

            if pattern[i]!=string[j]:
                if pattern[i]!="*" and pattern[i]!="?":
                    return False
                else:
                    if pattern[i]=="*":
                        dp[(i,j)]=helper(i+1,j+1) or helper(i,j+1) or helper(i+1,j)
                    else:
                        dp[(i,j)]=helper(i+1,j+1)
            else:
                dp[(i,j)]=helper(i+1,j+1)

            return dp[(i,j)]
        return helper(0,0)



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends