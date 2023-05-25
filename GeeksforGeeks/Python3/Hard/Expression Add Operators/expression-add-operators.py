#User function Template for python3

class Solution:
    def addOperators(self, S, target):
        # Code here
        res = []

        def helper(curr_idx, curr_res, curr_sum, prev):
            if curr_idx >= len(S):
                if curr_sum == target:
                    res.append("".join(curr_res))
                return
            
            for i in range(curr_idx, len(S)):
                curr_str = S[curr_idx:i+1]
                curr_S = int(curr_str)
                
                if not curr_res:
                    helper(i+1, [curr_str], curr_S, curr_S)
                else:
                    helper(i+1, curr_res + ["+"]+ [curr_str], curr_sum+curr_S, curr_S)
                    helper(i+1, curr_res + ["-"]+ [curr_str], curr_sum-curr_S, -curr_S)
                    helper(i+1, curr_res + ["*"]+ [curr_str], curr_sum-prev+ curr_S*prev, curr_S*prev)
                
                if S[curr_idx] == "0":
                    break
        
        helper(0, [], 0, 0)
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        S = input()
        target = int(input())
        ob = Solution()
        res = ob.addOperators(S, target)
        res.sort()
        for combination in res:
            print(combination, end = ' ')
        print()
# } Driver Code Ends