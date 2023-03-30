class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == len(set(arr)): return len(arr) - 1
        idxs = defaultdict(set)
        for i, v in enumerate(arr):
            idxs[v].add(i)
        
        pre, cur, seen = {-1}, {0}, set()
        for step in itertools.count():
            pre |= cur 
            if len(arr) - 1 in pre: 
                return step
            
            tmp = set()
            for i in cur:
                if i < 0 or i >= len(arr): continue
                if arr[i] not in seen:
                    tmp |= (idxs[arr[i]] - pre)
                    seen.add(arr[i])
                if i - 1 > 0 and i - 1 not in pre: tmp.add(i-1)
                if i + 1 < len(arr) and i + 1 not in pre: tmp.add(i+1)
            
            tmp -= pre
            pre |= tmp 
            cur = tmp