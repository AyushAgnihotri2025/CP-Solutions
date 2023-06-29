#User function Template for python3


class Solution:
    def digits_N(self, N):
        num = N
        digits = []
        while num:
            digits.append(num%10)
            num = num // 10
        return digits
    
    def check_happiness(self, N):
        num = N
        non_happy = []
        while num > 9:
            digits = self.digits_N(num)
            num = 0
            for i in digits:
                num += i*i
            if num in non_happy:
                return False
            non_happy.append(num)
        if num == 1:
            return True
        if num == 7:
            return True
        return False
    
    def nextHappy (self, N):
        # code here
        happy_flag = False
        while not happy_flag:
            N = N + 1
            if self.check_happiness(N):
                happy_flag = True
        return N

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.nextHappy(N))
# } Driver Code Ends