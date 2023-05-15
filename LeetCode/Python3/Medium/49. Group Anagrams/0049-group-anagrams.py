from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = 0
        label = []
        label_c = []
        for st in strs:
            cur = ''.join(sorted(st))
            if label.__contains__(cur):
                label_c.append(label_c[label.index(cur)])
            else:
                label_c.append(count)
                count += 1
            label.append(cur)

        tmp = 0
        result = []
        while tmp < count:
            result.append([])
            tmp += 1
        for i, c in enumerate(strs):
            result[label_c[i]].append(c)
            
        return result