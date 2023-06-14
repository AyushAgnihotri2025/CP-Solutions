#User function Template for python3
# Given below is the structure of Node class
# list moves from left to right
# class node:
#     def __init__(self):
#         self.data = None
#         self.left = None
#         self.right = None

class Solution:
    def mailDesign(self, N, Q, query):
        # code here
        unread=[i+1 for i in range(N)]
        cu=-1
        read=[]
        cr=-1
        ct=-1
        trash=[]
        def createll(l):
            start=None
            curr=None
            while(l):
                if start==None:
                    start=node()
                    start.data=l.pop(0)
                    curr=start
                else:
                    c=node()
                    c.data=l.pop(0)
                    curr.right=c
                    c.left=curr
                    curr=c
            if start==None:
                start=node()
                start.data="EMPTY"
            return start
        for i in range(0,2*Q,2):
            if query[i]==1:
                c=query[i+1]
                unread.remove(c)
                read.append(c)
            elif query[i]==2:
                c=query[i+1]
                read.remove(c)
                trash.append(c)
            elif query[i]==3:
                c=query[i+1]
                unread.remove(c)
                trash.append(c)
            elif query[i]==4:
                c=query[i+1]
                trash.remove(c)
                read.append(c)
        unr=createll(unread)
        rd=createll(read)
        tr=createll(trash)
        return [unr,rd,tr]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
    
def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end = " ")
        temp = temp.right
    print()
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, Q = [int(x) for x in input().split()]
        query = input().split()
        for i in range(2*Q):
            query[i] = int(query[i])
        
        ob = Solution()
        ans = ob.mailDesign(N, Q, query)
        for i in range(3):
            printlist(ans[i])
# } Driver Code Ends