#User function Template for python3

class Solution:
    def asteroidCollision(self, N, asteroids):
        # Code here
        stack = []
        for i in range(N):
            if len(stack)>0 and (stack[-1]>0 and asteroids[i]<0):
                if abs(stack[-1])<abs(asteroids[i]):
                    stack.pop()
                    flag=True
                    while len(stack)>0 and (stack[-1]>0 and asteroids[i]<0):
                        if abs(stack[-1])<abs(asteroids[i]):
                            stack.pop()
                        elif abs(stack[-1])==abs(asteroids[i]):
                            stack.pop()
                            flag=False
                            break
                        else:
                            flag=False
                            break
                    if flag:
                        stack.append(asteroids[i])
                    if len(stack)==0:
                        stack.append(asteroids[i])
                elif abs(stack[-1])==abs(asteroids[i]):
                    stack.pop()
            else:
                stack.append(asteroids[i])
        return stack


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends