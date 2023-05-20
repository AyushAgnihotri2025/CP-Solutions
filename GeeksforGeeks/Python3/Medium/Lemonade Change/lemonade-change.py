#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def lemonadeChange(self, N, bills):
        # Code here
        c1, c2, c3 = 0, 0, 0
        for bill in bills:
            if bill == 5:
                c1 += 1
            elif bill == 10:
                if c1 >= 1:
                    c1 -= 1
                    c2 += 1
                else:
                    return False
            elif bill == 20:
                if c2 >= 1 and c1 >= 1:
                    c2 -= 1
                    c1 -= 1
                    c3 += 1
                elif c1 >= 3:
                    c1 -= 3
                    c3 += 1
                else:
                    return False
        return True


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends