class Solution:
    def find(self, arr, n):
        # Your code goes here
        i = 0
        flag = True
        while flag:
            i += 1
            flag = False
            num = i
            for item in arr:
                num = num*2 - item
                if num < 0:
                    flag = True
                    break
        return i


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a=list(map(int,input().split()))
        ob = Solution()
        ans=ob.find(a,n)
        print(ans)
# } Driver Code Ends