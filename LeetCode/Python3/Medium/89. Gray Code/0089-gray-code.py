class Solution:
    def grayCode(self, n: int) -> List[int]:
        start_list = [0, 1]
        for i in range(2, n+1):
            summand = 2**(i-1)
            start_list = start_list+[elem+summand for elem in reversed(start_list)]
        return start_list