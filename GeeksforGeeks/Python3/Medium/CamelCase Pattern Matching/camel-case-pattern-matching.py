#User function Template for python3

class Solution:
    def CamelCase(self,N,Dictionary,Pattern):
        #code here
        trie = Node()
        for s in Dictionary:
            trie.insert(s)
        ret = trie.search(Pattern)
        return ret if ret else [-1]

class Node:
    def __init__(self):
        self.store = [None]*26
        self.words = []
        
    def insert(self, s):
        n = self
        for c in s:
            if c.islower():
                continue
            idx = ord(c)-ord('A')
            if not n.store[idx]:
                n.store[idx] = Node()
            n.store[idx].words.append(s)
            n = n.store[idx]
    
    def search(self, p):
        n = self
        for c in p:
            if c.islower():
                continue
            idx = ord(c)-ord('A')
            if not n.store[idx]:
                return False
            n = n.store[idx]
        return n.words

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Dictionary=list(map(str,input().split()))
        Pattern=input()
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends