class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei=defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
        visit=set([beginWord])
        q=deque([beginWord])
        count=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return count
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            count+=1
        return 0        