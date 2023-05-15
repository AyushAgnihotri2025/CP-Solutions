class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        result = 0
        for i, c1 in enumerate(num1):
            for j, c2 in enumerate(num2):
                result += int(c1) * int(c2) * pow(10, len1-i-1) * pow(10, len2-j-1)

        return str(result)