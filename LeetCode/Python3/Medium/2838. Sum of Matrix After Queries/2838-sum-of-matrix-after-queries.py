class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rowSeenCount, colSeenCount, total = 0, 0, 0
        rowSeen, colSeen = [False] * n, [False] * n
        for qi in range(len(queries) - 1, -1, -1):
            typei, index, val = queries[qi][0], queries[qi][1], queries[qi][2]
            if typei == 0 and not rowSeen[index]:
                rowSeenCount += 1
                rowSeen[index] = True
                total += (n - colSeenCount) * val
            if typei == 1 and not colSeen[index]:
                colSeenCount += 1
                colSeen[index] = True
                total += (n - rowSeenCount) * val
        return total