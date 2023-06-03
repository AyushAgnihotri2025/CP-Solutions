#User function Template for python3
class Solution:
    def min_sprinklers(self, gallery, n):
        # code here
        water = []
        for i in range(n):
            if gallery[i] != -1:
                water.append((i-gallery[i], i+gallery[i]))
        if len(water) == 0:
            return -1
        water.sort()
        ans = 0
        left, right = 0, 0
        if water[0][0] > right:
            return -1
        else:
            ans = 1
            right = water[0][1]
        for i in range(1, len(water)):
            if right >= n-1:
                break
            if water[i][0] <= left:
                right = max(right, water[i][1])
            elif water[i][0] > right+1:
                return -1
            else:
                ans += 1
                left = right+1
                right = water[i][1]
        return ans if right >= n-1 else -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        gallery = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.min_sprinklers(gallery,n))

# } Driver Code Ends