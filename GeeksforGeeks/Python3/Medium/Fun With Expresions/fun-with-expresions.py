#User function Template for python3

class Solution:
	def calculate(self, s):
		#Code here
		pri = {'*' : 2, '/' : 2, '+' : 1, '-' : 1}
        num = 0
        stack = []
        ops = []
        for c in s:
            if c in ['*', '/', '+', '-']:
                stack.append(num)
                num = 0
                while len(ops) > 0 and pri[ops[-1]] >= pri[c]:
                    op2 = stack.pop()
                    op1 = stack.pop()
                    op = ops.pop()
                    res = 0
                    if op == '*':
                        res = op1 * op2
                    elif op == '/':
                        res = int(op1 / op2)
                    elif op == '+':
                        res = op1 + op2
                    else:
                        res = op1 - op2
                    stack.append(res)
                ops.append(c)
            else:
                num = num * 10 + int(c)
        stack.append(num)
        while len(ops) > 0:
            op2 = stack.pop()
            op1 = stack.pop()
            op = ops.pop()
            res = 0
            if op == '*':
                res = op1 * op2
            elif op == '/':
                res = int(op1 / op2)
            elif op == '+':
                res = op1 + op2
            else:
                res = op1 - op2
            stack.append(res)
        return stack[0]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		obj = Solution()
		ans = obj.calculate(s)
		print(ans)

# } Driver Code Ends