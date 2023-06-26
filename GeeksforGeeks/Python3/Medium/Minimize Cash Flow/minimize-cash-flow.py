from typing import List

class Solution:
    def minCashFlow(self, n : int, g : List[List[int]]) -> List[List[int]]:
        # code here
        ans=[[0 for _ in range(n)] for _ in range(n)]
        graph=[[] for _ in range(n)]
        amounts=[0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if g[i][j]:
                    graph[i].append((j,g[i][j]))
        for i in range(n):
            size=len(graph[i])
            for j in range(size):
                v =  graph[i][j][0]
                w=  graph[i][j][1]
                amounts [i] -= w
                amounts[v] += w
        for i in range(n):
            maxCredit=maxDebit=0
            credit=debit=None
            for j in range(n):
                if amounts[j] > maxCredit:
                    credit=j
                    maxCredit=amounts[j]
                if amounts[j] < maxDebit:
                    debit=j
                    maxDebit=amounts[j]
            if maxCredit and maxDebit:
                if maxCredit >= abs(maxDebit):
                    ans[debit][credit]= abs(maxDebit)
                    amounts[debit] = 0
                    amounts[credit] -= abs(maxDebit)
                else:
                    ans[debit][credit]= maxCredit
                    amounts[debit] += maxCredit
                    amounts[credit] = 0
        return ans

#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        g=IntMatrix().Input(n, n)
        
        obj = Solution()
        res = obj.minCashFlow(n, g)
        
        IntMatrix().Print(res)
        

# } Driver Code Ends