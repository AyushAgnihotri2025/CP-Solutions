#User function Template for python3

class Solution:
    def formCoils(self, n):
        # code here 
        mat = lambda i,j : 4 * n * i + j + 1
        answer = [[],[]]
        def getAns(i,j, direction, ans):
            ans.append(mat(i,j))
            step = 2
            while 0 <= i < 4*n and 0 <= j < 4*n:
                temp = 1
                while temp <= step:
                    # 0->up, 1-> right, 2-> down, 3-> left
                    if direction == 0:
                        i = i - 1
                    elif direction == 1:
                        j = j + 1
                    elif direction == 2:
                        i = i + 1
                    else:
                        j = j - 1
                    ans.append(mat(i,j))   
                    temp += 1
                direction = (direction + 1)%4
                if direction == 0 or direction == 2:
                    step += 2
        direction = 0
        i = 2 * n
        j = 2 * n - 1
        getAns(i,j,direction, answer[0])
        answer[0].pop()
        direction = 2
        i = 2 * n -1
        j = 2 * n 
        getAns(i,j,direction, answer[1])
        answer[1].pop()
        return answer

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        ob = Solution()
        ptr = ob.formCoils(n)
        
        for i in range(2):
            print(*ptr[i])
# } Driver Code Ends