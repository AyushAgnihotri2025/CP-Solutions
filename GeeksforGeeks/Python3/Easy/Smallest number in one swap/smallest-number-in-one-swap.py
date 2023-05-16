#User function Template for python3

class Solution:
    def smallestNumber(self, num):
        # code here
        num = list(num)
        str_num = []
        for e in num:
            str_num.append(e)
        n = len(num)
        rightMin = [0]*n
        right = 0
        rightMin[n-1] = -1
        right = n-1
        for i in range(n-2, -1, -1):
            if num[i] >= num[right]:
                rightMin[i] = right
            else:
                rightMin[i] = -1
                right = i
        small = -1
        mini = 25555555555
        for i in range(1, n):
     
            if str_num[i] == '0':
                 
                for j in range(n-1, -1, -1):
                    if(mini > int(str_num[j]) and str_num[j] != '0'):
                        small = j
                        mini = int(str_num[j])
                str_num[0], str_num[small] = str_num[small], str_num[0]
                break
        for i in range(0, n):
            if(i != 0):
                if rightMin[i] != -1 and (num[i] != num[rightMin[i]]):
                    num[i], num[rightMin[i]] = num[rightMin[i]], num[i]
                    break
            else:
                if rightMin[i] != -1 and num[rightMin[i]] != '0' and num[i] != num[rightMin[i]]:
                    num[i], num[rightMin[i]] = num[rightMin[i]], num[i]
                    break
        ans1 =  ''.join(num)
        ans2 = ''.join(str_num)
        if(ans1 < ans2):
            return ans1
        else:
            return ans2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        ob = Solution()
        ans = ob.smallestNumber(s)
        print(ans)
# } Driver Code Ends