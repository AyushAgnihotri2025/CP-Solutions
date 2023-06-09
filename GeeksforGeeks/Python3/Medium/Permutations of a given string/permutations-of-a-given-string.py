#User function Template for python3

class Solution:
    def find_permutation(self, S):
        # Code here
        S = list(S)
        S.sort()
        permutations = []
        visited = [False] * len(S)
    
        def backtrack(path):
            if len(path) == len(S):
                permutations.append("".join(path))
                return
            for i in range(len(S)):
                if visited[i] or (i > 0 and S[i] == S[i - 1] and not visited[i - 1]):
                    continue
                visited[i] = True
                path.append(S[i])
                backtrack(path)
                path.pop()
                visited[i] = False
    
        backtrack([])
        return permutations

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends