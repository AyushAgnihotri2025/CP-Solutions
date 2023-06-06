#User function Template for python3

from math import log

def constructTree(postfix):
    #your code goes here
    digits = []
    for item in postfix:
        if item.isalpha():
            digits.append(item)
        else:
            item2 = digits.pop()
            item1 = digits.pop()
            digits.append(item1 + item + item2)
    start = et(0)
    stack = [(start, digits[0])]
    while stack:
        root, path = stack.pop()
        if len(path) == 1:
            root.value = path + ' '
            continue
        n = 2**int(log(len(path)+1, 2)-1) - 1
        root.value = path[n] + ' '
        root.left = et(0)
        root.right = et(0)
        stack.append((root.left, path[:n]))
        stack.append((root.right, path[n+1:]))
    return start

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class et():
	def __init__(self, x):
		self.value= x
		self.left = None
		self.right = None

def isOperator(c):

	if (c == '+' or c == '-' or c == '*' or c == '/' or c == '^'):
		return True
	return False


def inorder(t):
	if t:
		inorder(t.left)
		print(t.value,end = "")
		inorder(t.right)




for _ in range(int(input())):
	postfix = input()
	r = constructTree(postfix)
	inorder(r)
	print()

# } Driver Code Ends