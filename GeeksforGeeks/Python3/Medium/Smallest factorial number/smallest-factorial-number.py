#User function Template for python3

class Solution:
    def findNum(self, n : int):
        # Complete this function
        count=0
        num=5
        while True:
            temp=num
            while temp%5==0:
                count+=1
                temp//=5
            if count>=n:
                return num
            num+=5

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.findNum(n))
# } Driver Code Ends