# You are required to complete this fucntion
# Function should return the an integer
def findK(arr, n, m, k):
  #Code here
  top = 0
  left = 0
  bottom = n - 1
  right = m - 1
  dir = 1
  find_count = 1

  while top <= bottom and right >= left:
    if dir == 1:
      for i in range(left, right + 1):
        if find_count == k:
          return arr[top][i]
        find_count += 1
      top += 1
      dir = 2
    elif dir == 2:
      for i in range(top, bottom + 1):
        if find_count == k:
          return arr[i][right]
        find_count += 1
      right -= 1
      dir = 3
    elif dir == 3:
      for i in range(right, left - 1, -1):
        if find_count == k:
          return arr[bottom][i]
        find_count += 1
      bottom -= 1
      dir = 4
    else:
      for i in range(bottom, top - 1, -1):
        if find_count == k:
          return arr[i][left]
        find_count += 1
      left += 1
      dir = 1

  return None


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        print(findK(matrix, n[0], n[1], n[2]))
# } Driver Code Ends