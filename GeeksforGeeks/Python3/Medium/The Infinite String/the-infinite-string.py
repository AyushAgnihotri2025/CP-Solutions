#User function Template for python3
class Solution:
    def posInfinite (self, pos):
        # code here 
        li = [5]
        num = 5
        for i in range(1,41):
            num = num*2 + i
            li.append(num)
        return self.find_(pos,li)
        
    def find_(self,pos,li):
        if pos <= 11:
            if pos <= 5:
                return str(pos)
            elif pos == 6:
                return '$'
            elif pos > 6:
                return str(11-pos+1)
        l = len(li)
        brp =0
        for i in range(l):
            if li[i]<=pos and li[i+1] >= pos:
                brp = i
                break
        if li[brp]+brp+1 >= pos:
            return '$'
        else:
            return self.find_(pos-(li[brp]+brp+1),li)
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        pos = int(input())
        
        ob = Solution()
        print(ob.posInfinite(pos))
# } Driver Code Ends