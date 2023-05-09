from typing import List

# Added
from itertools import combinations


class Solution:
    def minDifference(self, n : int, arr : List[int]) -> List[List[int]]:
        # code here
        total = sum(arr)
        s1 = s2 = 0
        min_diff = float("inf")
        for subset in combinations(arr, n // 2):
            sum1 = sum(subset)
            sum2 = total - sum1
            if sum1 > sum2:
                sum1, sum2 = sum2, sum1
            diff = abs(sum2 - sum1)
            if diff < min_diff:
                min_diff = diff
                s1, s2 = sum1, sum2
        return [[s1], [s2]]

def Helper(arr, n, curr_elements, no_of_selected_elements, 
            soln, min_diff, Sum, curr_sum, curr_position):
    if (curr_position == n): 
        return
    if ((int(n / 2) - no_of_selected_elements) > 
                          (n - curr_position)):
        return

    Helper(arr, n, curr_elements, no_of_selected_elements, 
            soln, min_diff, Sum, curr_sum, curr_position + 1) 
    no_of_selected_elements += 1
    curr_sum = curr_sum + arr[curr_position] 
    curr_elements[curr_position] = True

    if (no_of_selected_elements == int(n / 2)):
        if (abs(int(Sum / 2) - curr_sum) < min_diff[0]):
            min_diff[0] = abs(int(Sum / 2) - curr_sum)
            for i in range(n):
                soln[i] = curr_elements[i]
    else:
        Helper(arr, n, curr_elements, no_of_selected_elements, 
                soln, min_diff, Sum, curr_sum, curr_position + 1)
    curr_elements[curr_position] = False


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
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.minDifference(n, arr)
        
        IntMatrix().Print(res)
        

# } Driver Code Ends