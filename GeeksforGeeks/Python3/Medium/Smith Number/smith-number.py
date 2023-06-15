#User function Template for python3

class Solution:
    def smithNum(self, n):
        # code here 
        def f(n):
            if n == 0 or n == 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        if f(n):
            return 0
        temp = sum(map(int, str(n)))
        div = 2
        cnt = 0
        while n > 1:
            if n % div == 0:
                n //= div
                cnt += sum(map(int, str(div)))
            else:
                div += 1
        return 1 if cnt == temp else 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        ob = Solution()
        print(ob.smithNum(n))
# } Driver Code Ends