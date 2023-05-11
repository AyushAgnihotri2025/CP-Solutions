#User function Template for python3

class Solution:

    def removeKdigits(self, S, K):
        # code here
        answer = ""
        for ch in S:
            while answer and answer[-1] > ch and K > 0:
                answer = answer[:-1]
                K -= 1
            if answer or ch != "0":
                answer += ch
        while answer and K > 0:
            answer = answer[:-1]
            K -= 1
        if not answer:
            return "0"
        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends