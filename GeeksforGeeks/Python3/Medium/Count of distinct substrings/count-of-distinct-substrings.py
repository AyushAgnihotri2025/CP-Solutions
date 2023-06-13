#User function Template for python3

def countDistinctSubstring(s):
    #code here
    se=set()
    se.add("")
    se.add(str(s[0]))
    for i in range(1,len(s)):
        se.add(str(s[i]))
        for j in range(i):
            se.add(str(s[j:i+1]))
            se.add(str(s[j]))
    return len(se)

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        print(countDistinctSubstring(s))
# } Driver Code Ends