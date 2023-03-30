class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        counter = 0
        last_number = 0
        for i in range(n):
            if arr[i] - last_number > 1:
                counter += arr[i] - last_number - 1
            last_number = arr[i]
            if counter >= k:
                return last_number - (counter - k + 1)
        return last_number + k - counter