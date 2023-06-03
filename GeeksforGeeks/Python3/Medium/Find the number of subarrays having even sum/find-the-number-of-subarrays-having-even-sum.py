#User function Template for python3

class Solution:
    def countEvenSum(self, arr, n):
        # code here
        es=0
        os=0
        s=0
        for i in arr:
            s=s+i
            if s%2==0:
               es+=1
            else:
                os+=1
        c=(os*(os-1))//2+(es*(es-1))//2+es           
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countEvenSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends