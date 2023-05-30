#User function Template for python3

class Solution:
    def isValid(self, boardboard):
        # code here
        bb = [[0,0,0] for i in range(3)]
        j = 0
        bb[0][0] = board[0]
        bb[0][1] = board[1]
        bb[0][2] = board[2]
        bb[1][0] = board[3]
        bb[1][1] = board[4]
        bb[1][2] = board[5]
        bb[2][0] = board[6]
        bb[2][1] = board[7]
        bb[2][2] = board[8]
        c = [0,0]
        for i in bb:
            for j in i:
                if j == 'X':
                    c[0]+=1
                else:
                    c[1]+=1
        if c[0] != c[1]+1 and c[0]!=c[1]:
            return 0
        xwin = False
        owin = False
        for i in bb:
            if i[0]==i[1]==i[2]:
                if i[0]=='X':
                    xwin = True
                else:
                    owin = True
        for i in range(3):
            if bb[0][i] == bb[1][i] == bb[2][i]:
                if bb[0][i] == 'X':
                    xwin = True
                else:
                    owin = True
        if bb[0][0] == bb[1][1] == bb[2][2]:
            if bb[0][0] == 'X':
                xwin = True
            else:
                owin = True
        if bb[0][2] == bb[1][1] == bb[2][0]:
            if bb[1][1] == 'X':
                xwin = True
            else:
                owin = True
        if xwin and owin:
            return False
        if owin and c[0] != c[1]:
            return False
        if xwin and c[0] != c[1]+1:
            return False
        return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        board = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.isValid(board)
        if ans:
            print("Valid")
        else:
            print("Invalid")
        tc -= 1

# } Driver Code Ends