#User function Template for python3

class Solution:
    def increasingNumbers(self, N):
    	#code here
        self.ans = []
        def recursion(start, num):
            if num >= pow(10, N):
                return
            if len(str(num)) == N:
                self.ans.append(num)
            for i in range(start, 10):
                num = num*10 + i
                recursion(i+1, num)
                num //= 10
        recursion(1, 0)
        return self.ans

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.increasingNumbers(N)
        for num in ans:
            print(num,end=' ')
        print()
# } Driver Code Ends