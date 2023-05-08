#User function Template for python3

class Solution():
    def modulo(self, s, m):
        #your code goes here
        res = 0
        for i in s: res = (res*2 + int(i))%m
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s,m = input().split()
        m = int(m)
        print(Solution().modulo(s, m))

# } Driver Code Ends