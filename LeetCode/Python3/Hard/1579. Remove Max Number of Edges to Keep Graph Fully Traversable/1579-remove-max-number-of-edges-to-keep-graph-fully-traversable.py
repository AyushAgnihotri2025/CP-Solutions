class UF:
    def __init__(self, n):
        self.count = n
        self.arr = [i for i in range(n)]

    def find(self, a):
        if a != self.arr[a]:
            self.arr[a] = self.find(self.arr[a])
        return self.arr[a]

    def union(self, a, b):
        if self.find(a) != self.find(b):
            self.arr[self.find(a)] = self.find(b)
            self.count -= 1
            return True
        return False

    def united(self):
        return self.count == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: x[0], reverse=True)
        A = UF(n)
        B = UF(n)
        res = 0
        for edge in edges:
            if edge[0] == 3:
                # alice and bob
                a = A.union(edge[1] - 1, edge[2] - 1)
                b = B.union(edge[1] - 1, edge[2] - 1)
                if not a and not b:
                    res += 1
            elif edge[0] == 2:
                # bob
                if not B.union(edge[1] - 1, edge[2] - 1):
                    res += 1
            else:
                # alice
                if not A.union(edge[1] - 1, edge[2] - 1):
                    res += 1
        return res if B.united() and A.united() else -1