class Solution:
    def are_similar(s1, s2):
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        diff = [(c1, c2) for c1, c2 in zip(s1, s2) if c1 != c2]
        return len(diff) == 2 and diff[0] == diff[1][::-1]

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i+1, n):
                if Solution.are_similar(strs[i], strs[j]):
                    uf.union(i, j)

        return len(set(uf.find(i) for i in range(n)))

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.parent[pi] = pj
