import math

class Solution:
    def count (self, N):
        # code here 
        box='%s'%bin(N)
        num=box.count('1')
        ans=0
        for i in range(2,len(box)-1):
            q=len(box[i+1:len(box)])
            if num>q:
                continue
            if box[i]=='1':
                ans+=int(math.factorial(q)/(math.factorial(num)*math.factorial(q-num)))
                num-=1
        return ans



#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N = int(input())
        print(ob.count(N))



# } Driver Code Ends