class Solution:        
    def find(self, dsuf: List[int], idx: int) -> int:
        if dsuf[idx] == -1:
            return idx
        dsuf[idx] = self.find(dsuf, dsuf[idx])
        return dsuf[idx]

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        dsuf = [-1] * n
        count = 0
        # Run for all edges
        for it in connections:
            parentTo = self.find(dsuf, it[0])
            parentFrom = self.find(dsuf, it[1])
            if parentTo != parentFrom:
                if parentTo < parentFrom:
                    dsuf[parentTo] = parentFrom
                else:
                    dsuf[parentFrom] = parentTo
                count += 1
        return n - count - 1