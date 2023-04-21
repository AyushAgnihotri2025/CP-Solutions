#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def prefixSuffixString(self, s1, s2) -> int:
        #code here
        count=0
        suffix=set()
        for i in range(len(s1)):
            for j in range(1,len(s1[i])):
                suffix.add(s1[i][j:])
                
        prefix=set()
        for i in range(len(s1)):
            for j in range(1,len(s1[i])):
                prefix.add(s1[i][:j])
                
        for s in s2:
            if s in suffix or s in prefix:
                count+=1
                
        return count
        

#{ 
 # Driver Code Starts.

if __name__=="__main__":
    for _ in range(int(input())):
        s1 = list(map(str, input().split()))
        s2 = list(map(str, input().split()))
        obj=Solution()
        print(obj.prefixSuffixString(s1, s2))
# } Driver Code Ends