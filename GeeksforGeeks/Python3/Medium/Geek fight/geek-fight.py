from typing import List

class Solution:
    def win(self, n : int, power : List[int], q : int, Q : List[int]) -> List[List[int]]:
        # code here
        def binary(arr,ele):
            lo,hi = 0,len(arr)-1
            ans = -1
            while lo<=hi:
                mid = (lo+hi)//2
                if arr[mid]<=ele:
                    ans = mid
                    lo = mid+1
                else:
                    hi = mid-1
            return ans
        power = sorted(power)
        ans = power[::]
        for i in range(1,n):
            ans[i] += ans[i-1]
        a = []
        for i in range(q):
            ele = Q[i]
            idx = binary(power,ele)
            if idx==-1:
                a.append((0,0))
                continue
            a.append((idx+1,ans[idx]))
        return a

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
        
        
        power=IntArray().Input(n)
        
        
        q = int(input())
        
        
        Q=IntArray().Input(q)
        
        obj = Solution()
        res = obj.win(n, power, q, Q)
        
        IntMatrix().Print(res)
        

# } Driver Code Ends