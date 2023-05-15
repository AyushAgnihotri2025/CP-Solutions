class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        string = '1'
        temp = ''
        count = 0
        for _ in range(n-1):
            s = string[0]
            for l in string:
                if l==s:
                    count += 1
                else:
                    temp += str(count)+s
                    s = l
                    count = 1
            temp += str(count)+l
            string = temp
            temp = ''
            count = 0
        return string