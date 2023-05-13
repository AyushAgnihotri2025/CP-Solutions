from typing import List

class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        # code here
        price1, count, pos = sorted([[price[i], i+1] for i in range(n)]), 0, 0
        while k>0 and pos<n:
            if k<price1[pos][0]:
                break
            elif k>=price1[pos][0]*price1[pos][1]:
                k-=price1[pos][0]*price1[pos][1]
                count+=price1[pos][1]
                pos+=1
            else:
                price1[pos][1]-=1
        return count
        



#{ 
 # Driver Code Starts


class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)
        

# } Driver Code Ends