#User function Template for python3
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        N = len(s)
        stack, ans, curr = [], set(), []
        reslen = [0]

        def solve(i, rl):
            if i == N:
                if not stack:
                    if rl > reslen[0]:
                        ans.clear()
                        reslen[0] = rl
                    if rl >= reslen[0]:
                        ans.add("".join(curr))
                return
            if s[i] not in '()':
                curr.append(s[i])
                solve(i+1,rl+1)
                curr.pop()
                return

            if s[i] == ')' and stack:
                curr.append(')')
                stack.pop()
                solve(i+1,rl+1)
                stack.append('(')
                curr.pop()
            elif s[i] == '(':
                stack.append('(')
                curr.append('(')
                solve(i+1,rl+1)
                stack.pop()
                curr.pop()
            solve(i+1, rl)

        solve(0,0)
        return sorted(list(ans))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range (int(input())):
    s = input().strip()
    ob = Solution()
    a = ob.removeInvalidParentheses(s)
    a.sort()
    print(*a)
# } Driver Code Ends