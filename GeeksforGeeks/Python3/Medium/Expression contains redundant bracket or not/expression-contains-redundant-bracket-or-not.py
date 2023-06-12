class Solution():
    def checkRedundancy(self, s):
        #your code goes here
        stack = []
        for a in s:
            if a == ')':
                has_operation = False
                while stack:
                    ele = stack.pop()
                    if ele in ['+', '-', '*', '/']:
                        has_operation = True
                    if ele == '(':
                        break
                if has_operation is False:
                    return 1
            else:
                stack.append(a)
        return 0

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        print(Solution().checkRedundancy(s))

# } Driver Code Ends