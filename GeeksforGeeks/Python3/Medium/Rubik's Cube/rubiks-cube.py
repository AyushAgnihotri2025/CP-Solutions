def clockwise(up):
    x, y, z = up[0][0], up[0][1], up[0][2]
    up[0][0], up[0][1], up[0][2] = up[2][0], up[1][0], up[0][0]
    up[2][0], up[1][0], up[0][0] = up[2][2], up[2][1], up[2][0]
    up[2][2], up[2][1], up[2][0] = up[0][2], up[1][2], up[2][2]
    up[0][2], up[1][2], up[2][2] = x, y, z
    
def anticlockwise(up):
    x, y, z = up[0][0], up[0][1], up[0][2]
    up[0][0], up[0][1], up[0][2] = up[0][2], up[1][2], up[2][2]
    up[0][2], up[1][2], up[2][2] = up[2][2], up[2][1], up[2][0]
    up[2][2], up[2][1], up[2][0] = up[2][0], up[1][0], up[0][0]
    up[2][0], up[1][0], up[0][0] = x, y, z

def rotate(move, up, front, left, right, back, down):
    for m in move:
        if m == 'U':
            clockwise(up)
            x, y, z = back[0][2], back[0][1], back[0][0]
            back[0][2], back[0][1], back[0][0] = left[0][2], left[0][1], left[0][0]
            left[0][2], left[0][1], left[0][0] = front[0][2], front[0][1], front[0][0]
            front[0][2], front[0][1], front[0][0] = right[0][2], right[0][1], right[0][0]
            right[0][2], right[0][1], right[0][0] = x, y, z
        elif m == 'Ui':
            anticlockwise(up)
            x, y, z = right[0][2], right[0][1], right[0][0]
            right[0][2], right[0][1], right[0][0] = front[0][2], front[0][1], front[0][0]
            front[0][2], front[0][1], front[0][0] = left[0][2], left[0][1], left[0][0]
            left[0][2], left[0][1], left[0][0] = back[0][2], back[0][1], back[0][0]
            back[0][2], back[0][1], back[0][0] = x, y, z
        elif m == 'B':
            clockwise(back)
            x, y, z = up[0][2], up[0][1], up[0][0]
            up[0][2], up[0][1], up[0][0] = right[2][2], right[1][2], right[0][2]
            right[2][2], right[1][2], right[0][2] = down[2][0], down[2][1], down[2][2]
            down[2][0], down[2][1], down[2][2] = left[0][0], left[1][0], left[2][0]
            left[0][0], left[1][0], left[2][0] = x, y, z
        elif m == 'Bi':
            anticlockwise(back)
            x, y, z = left[0][0], left[1][0], left[2][0]
            left[0][0], left[1][0], left[2][0] = down[2][0], down[2][1], down[2][2]
            down[2][0], down[2][1], down[2][2] = right[2][2], right[1][2], right[0][2]
            right[2][2], right[1][2], right[0][2] = up[0][2], up[0][1], up[0][0]
            up[0][2], up[0][1], up[0][0] = x, y, z
        elif m == 'F':
            clockwise(front)
            x, y, z = up[2][0], up[2][1], up[2][2]
            up[2][0], up[2][1], up[2][2] = left[2][2], left[1][2], left[0][2]
            left[2][2], left[1][2], left[0][2] = down[0][2], down[0][1], down[0][0]
            down[0][2], down[0][1], down[0][0] = right[0][0], right[1][0], right[2][0]
            right[0][0], right[1][0], right[2][0] = x, y, z
        elif m == 'Fi':
            anticlockwise(front)
            x, y, z = right[0][0], right[1][0], right[2][0]
            right[0][0], right[1][0], right[2][0] = down[0][2], down[0][1], down[0][0]
            down[0][2], down[0][1], down[0][0] = left[2][2], left[1][2], left[0][2]
            left[2][2], left[1][2], left[0][2] = up[2][0], up[2][1], up[2][2]
            up[2][0], up[2][1], up[2][2] = x, y, z
        elif m == 'D':
            clockwise(down)
            x, y, z = front[2][0], front[2][1], front[2][2]
            front[2][0], front[2][1], front[2][2] = left[2][0], left[2][1], left[2][2]
            left[2][0], left[2][1], left[2][2] = back[2][0], back[2][1], back[2][2]
            back[2][0], back[2][1], back[2][2] = right[2][0], right[2][1], right[2][2]
            right[2][0], right[2][1], right[2][2] = x, y, z
        elif m == 'Di':
            anticlockwise(down)
            x, y, z = right[2][0], right[2][1], right[2][2]
            right[2][0], right[2][1], right[2][2] = back[2][0], back[2][1], back[2][2]
            back[2][0], back[2][1], back[2][2] = left[2][0], left[2][1], left[2][2]
            left[2][0], left[2][1], left[2][2] = front[2][0], front[2][1], front[2][2]
            front[2][0], front[2][1], front[2][2] = x, y, z
        elif m == 'L':
            clockwise(left)
            x, y, z = back[2][2], back[1][2], back[0][2]
            back[2][2], back[1][2], back[0][2] = down[0][0], down[1][0], down[2][0]
            down[0][0], down[1][0], down[2][0] = front[0][0], front[1][0], front[2][0]
            front[0][0], front[1][0], front[2][0] = up[0][0], up[1][0], up[2][0]
            up[0][0], up[1][0], up[2][0] = x, y, z
        elif m == 'Li':
            anticlockwise(left)
            x, y, z = up[0][0], up[1][0], up[2][0]
            up[0][0], up[1][0], up[2][0] = front[0][0], front[1][0], front[2][0]
            front[0][0], front[1][0], front[2][0] = down[0][0], down[1][0], down[2][0]
            down[0][0], down[1][0], down[2][0] = back[2][2], back[1][2], back[0][2]
            back[2][2], back[1][2], back[0][2] = x, y, z
        elif m == 'R':
            clockwise(right)
            x, y, z = up[2][2], up[1][2], up[0][2]
            up[2][2], up[1][2], up[0][2] = front[2][2], front[1][2], front[0][2]
            front[2][2], front[1][2], front[0][2] = down[2][2], down[1][2], down[0][2]
            down[2][2], down[1][2], down[0][2] = back[0][0], back[1][0], back[2][0]
            back[0][0], back[1][0], back[2][0] = x, y, z
        elif m == 'Ri':
            anticlockwise(right)
            x, y, z = back[0][0], back[1][0], back[2][0]
            back[0][0], back[1][0], back[2][0] = down[2][2], down[1][2], down[0][2]
            down[2][2], down[1][2], down[0][2] = front[2][2], front[1][2], front[0][2]
            front[2][2], front[1][2], front[0][2] = up[2][2], up[1][2], up[0][2]
            up[2][2], up[1][2], up[0][2] = x, y, z
            
def construct(up, front, left, right, back, down):
    ans = []
    ans.append("UP")
    ans.append(''.join(c for line in up for c in line))
    ans.append("FRONT")
    ans.append(''.join(c for line in front for c in line))
    ans.append("LEFT")
    ans.append(''.join(c for line in left for c in line))
    ans.append("RIGHT")
    ans.append(''.join(c for line in right for c in line))
    ans.append("BACK")
    ans.append(''.join(c for line in back for c in line))
    ans.append("DOWN")
    ans.append(''.join(c for line in down for c in line))
    return ans

def newFormation(present, move, n):
    # Your code goes here
    up = [[' ' for _ in range(3)] for _ in range(3)]
    front = [[' ' for _ in range(3)] for _ in range(3)]
    left = [[' ' for _ in range(3)] for _ in range(3)]
    right = [[' ' for _ in range(3)] for _ in range(3)]
    back = [[' ' for _ in range(3)] for _ in range(3)]
    down = [[' ' for _ in range(3)] for _ in range(3)]
    for k in range(0, 12, 2):
        s = present[k].strip()
        if s == "UP":
            for i in range(3):
                for j in range(3):
                    up[i][j] = present[k+1][i*3+j]
        elif s == "FRONT":
            for i in range(3):
                for j in range(3):
                    front[i][j] = present[k+1][i*3+j]
        elif s == "LEFT":
            for i in range(3):
                for j in range(3):
                    left[i][j] = present[k+1][i*3+j]
        elif s == "RIGHT":
            for i in range(3):
                for j in range(3):
                    right[i][j] = present[k+1][i*3+j]
        elif s == "BACK":
            for i in range(3):
                for j in range(3):
                    back[i][j] = present[k+1][i*3+j]
        elif s == "DOWN":
            for i in range(3):
                for j in range(3):
                    down[i][j] = present[k+1][i*3+j]
    rotate(move, up, front, left, right, back, down)
    ans = construct(up, front, left, right, back, down)
    return ans

#{ 
 # Driver Code Starts

def main():

    T = int(input())

    while(T > 0):
        present = []
        for x in range(12):
            present.append(input())
            
        n = int(input())
        move = input().split()
        
        ans = []
        ans = newFormation(present, move, n)
        
        print(*ans, sep='\n')

        T -= 1


if __name__ == "__main__":
    main()




    
# } Driver Code Ends